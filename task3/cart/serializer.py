from rest_framework import serializers
from . import models


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CartSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
