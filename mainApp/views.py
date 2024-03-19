from django.shortcuts import render
from django.views import View

from mainApp.models import Category, SubCategory


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home.html')
        return render(request, 'home-unauth.html')


class Categories(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'subCategories': SubCategory.objects.all()
        }
        return render(request, 'categories.html', context)
