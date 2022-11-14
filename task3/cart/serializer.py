from rest_framework import serializers
from . import models


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class ProductSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CartSerial(serializers.ModelSerializer):
    productview = ProductSerial(source='Product', read_only=True)

    class Meta:
        model = models.Cart
        fields = [
            'productview',
            'owner',
            'prod_name',
            ]


class CustLocalSerial(serializers.ModelSerializer):
    class Meta:
        model = models.UserLocation
        fields = '__all__'
