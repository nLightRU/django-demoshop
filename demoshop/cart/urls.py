from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_page, name='cart_summary'),
    path('add', views.cart_add, name='cart_add'),
    path('reset', views.cart_reset, name='cart_reset')
]
