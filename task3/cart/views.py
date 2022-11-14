from rest_framework import generics, permissions
from . import serializer, models


class CreateCart(generics.CreateAPIView):
    serializer_class = serializer.CartSerial


class CartFull(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.CartSerial
    queryset = models.Cart.objects.filter(pk=1)


class CreateLocalCustomer(generics.CreateAPIView):
    serializer_class = serializer.CustLocalSerial


class LocalCustomerAPI(generics.RetrieveUpdateAPIView):
    serializer_class = serializer.CustLocalSerial
    queryset = models.UserLocation.objects.filter(pk=1)
