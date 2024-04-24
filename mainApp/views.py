from django.shortcuts import render
from django.views import View

from .models import *


class Home(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all(),
        }
        # if request.user.is_authenticated and request.user.confirmed:
        return render(request, 'home.html', context)
        # return render(request, 'home-unauth.html', context)


class Categories(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'subCategories': SubCategory.objects.all()
        }
        return render(request, 'categories.html', context)


class Products(View):
    def get(self, request):
        products = Product.objects.all()
        if request.GET.get("category_id"):
            products = products.filter(subCategory__category__id=request.GET.get("category_id"))
        if request.GET.get("subCategory_id"):
            products = products.filter(subCategory__id=request.GET.get("subCategory_id"))
        context = {
            'products': products
        }
        return render(request, 'products.html', context)


class ProductDetailsView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
            'rating': product.rating * 20,
            'discount_price': round(product.price * (1 - product.discount / 100), 2),
        }
        return render(request, 'product.html', context)


def page_blank_starter(request):
    return render(request, 'yana/page-blank-starter.html')


def page_components(request):
    return render(request, 'yana/page-components.html')


def page_content(request):
    return render(request, 'yana/page-content.html')


def listing_large(request):
    return render(request, 'yana/page-listing-large.html')


def offers(request):
    return render(request, 'yana/page-offers.html')


def payment(request):
    return render(request, 'yana/page-payment.html')


def profile_address(request):
    return render(request, 'yana/page-profile-address.html')


def profile_main(request):
    return render(request, 'yana/page-profile-main.html')


def profile_orders(request):
    return render(request, 'yana/page-profile-orders.html')