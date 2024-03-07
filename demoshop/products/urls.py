from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='home'),
     path('about', views.about, name='about'),
     path('register', views.register_user, name='register'),
     path('products/phones/<brand>', views.phones_brand, name='phones_by_brand'),
     path('products/phones', views.phones, name='phones'),
     path('products/', views.products)
]