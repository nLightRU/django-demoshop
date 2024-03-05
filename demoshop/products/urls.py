from django.urls import path

from . import views

urlpatterns = [
     path('', views.index),
     path('products/phones/<brand>', views.phones_brand),
     path('products/phones', views.phones),
     path('products/', views.products)
]