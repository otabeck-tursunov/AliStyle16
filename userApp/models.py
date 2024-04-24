from django.db import models
from django.contrib.auth.models import AbstractUser
from mainApp.models import *


class Profil(AbstractUser):
    GENDER = (('M', 'Male'), ('F', 'Female'))
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateField(blank=True, null=True)
    confirmation_code = models.PositiveSmallIntegerField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class ProductRate(models.Model):
    grade = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=5)
    text = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)

    # def save(self, *args, **kwargs):
    #     super(ProductRate, self).save(*args, **kwargs)
    #     self.product.update_rating()

    def __str__(self):
        return f"{self.product.name}: {self.grade}"
