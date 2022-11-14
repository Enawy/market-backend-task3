from django.urls import path
from cart import views


urlpatterns = [
    path('cart/', views.CreateCart.as_view()),
    path('cart/<int:pk>', views.CartFull.as_view()),
    path('location/', views.CreateLocalCustomer.as_view()),
    path('location/<int:pk>', views.LocalCustomerAPI.as_view()),
]


