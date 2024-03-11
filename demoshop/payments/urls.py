from django.urls import path

from . import views

urlpatterns = [
     path('payment_create', views.create_payment, name='payment create'),
]