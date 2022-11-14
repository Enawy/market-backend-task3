from django.db import models
from django.contrib.auth.models import User
# added placeholder for product.


class Product(models.Model):
    prod_name = models.CharField(max_length=50)


class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    prod_name = models.ManyToManyField(Product)
