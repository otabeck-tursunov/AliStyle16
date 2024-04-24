from django.contrib import admin
from .models import *

admin.site.register([Country, City, Category, SubCategory, ProductImage])


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'amount']
    inlines = [ProductImageInline]

# admin.site.register(Product, ProductAdmin)
