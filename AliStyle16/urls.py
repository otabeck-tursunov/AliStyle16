from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('order/', include('orderApp.urls')),

    path('', Home.as_view(), name='home'),



    path('blank-starter/', page_blank_starter, name='about-keraksiz'),
    path('components/', page_components, name='keraksiz'),
    path('content/', page_content, name='page-about'),
    path('listing-large/', listing_large, name='page-products-katta'),
    path('offers/', offers, name='page-takliflar'),
    path('payment/', payment, name='page-tolov-keraksiz'),
    path('profile-address/', profile_address, name='page-adreslar-keraksiz'),
    path('profile-main/', profile_main, name='page-profile'),
    path('profile-orders/', profile_orders, name='page-buyurtmalar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
