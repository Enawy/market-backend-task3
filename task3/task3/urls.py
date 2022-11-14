from django.contrib import admin
from django.urls import path, include
from cart import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
]
