from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', Categories.as_view(), name='categories'),
    path('products/', Products.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailsView.as_view()),
]