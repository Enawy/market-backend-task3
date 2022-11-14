from rest_framework import generics, permissions
from . import serializer, models


class CreateCart(generics.CreateAPIView):
    serializer_class = serializer.CartSerial


class CartFull(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.CartSerial
    queryset = models.Cart.objects.filter(pk=1)