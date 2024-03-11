from django.urls import path

from . import views

urlpatterns = [
     path('payment_success', views.payment_succsess, name='payment_succsess'),
]