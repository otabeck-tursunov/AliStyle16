from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from eskiz.client import SMSClient
from AliStyle16 import settings


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        profil = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        print(profil)
        if profil is not None:
            if profil.confirmed:
                login(request, profil)
                print("login boldi")
                return redirect('home')
            return redirect('confirm')
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        context = {
            'cities': City.objects.all(),
            'countries': Country.objects.all()
        }
        return render(request, 'register.html', context)

    def post(self, request):
        from random import randrange
        if request.POST.get('password1') != request.POST.get('password2'):
            return redirect('register')
        code = randrange(111111, 999999)
        profil = Profil.objects.create_user(
            username=request.POST.get('phone_number'),
            password=request.POST.get('password1'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name', None),
            phone_number=request.POST.get('phone_number'),
            gender=request.POST.get('gender'),
            city=City.objects.get(id=request.POST.get('city')),
            country=Country.objects.get(id=request.POST.get('country')),
            confirmation_code=code
        )
        login(request, profil)
        client = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email=str(settings.ESKIZ_EMAIL),
            password=str(settings.ESKIZ_TOKEN)
        )

        response = client._send_sms(
            phone_number=f"{request.POST.get('phone_number')}",
            message=f"{code}"
        )
        return redirect('confirm')


class ConfirmView(View):
    def get(self, request):
        return render(request, 'confirm.html')

    def post(self, request):
        if request.user.is_authenticated:
            profil = request.user
            print(profil.confirmation_code)
            if profil.confirmation_code == int(request.POST.get('code')):
                print(request.POST.get('code'))
                profil.confirmed = True
                profil.save()
                logout(request)
                return redirect('login')
            return redirect('confirm')
        return redirect('register')


