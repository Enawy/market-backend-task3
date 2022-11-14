from django.db import models
from django.contrib.auth.models import User
# added placeholder for product.


class Product(models.Model):
    prod_name = models.CharField(max_length=50)

    def __str__(self):
        return self.prod_name


class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    prod_name = models.ManyToManyField(Product)


class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    apartment = models.IntegerField()