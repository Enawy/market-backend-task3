from django.urls import path
from cart import views


urlpatterns = [
    path('', views.CreateCart.as_view()),
    path('<int:pk>', views.CartFull.as_view()),
]


