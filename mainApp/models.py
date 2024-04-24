from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subCategories/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0)])
    brand = models.CharField(max_length=255)
    discount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    description = models.TextField(blank=True, null=True)
    guaranty = models.CharField(max_length=255)
    deliver = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=1)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    min_order = models.PositiveIntegerField(default=1)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

    # def update_rating(self):
    #     average_rating = self.productrate_set.aggregate(Avg('grade'))['grade__avg']
    #     self.rating = average_rating if average_rating is not None else None
    #     self.save()
    #
    # def save(self, *args, **kwargs):
    #     super(Product, self).save(*args, **kwargs)
    #     self.update_rating()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product.name


class Parametr(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}: {self.value}"
