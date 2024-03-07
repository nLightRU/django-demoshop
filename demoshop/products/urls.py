from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='home'),
     path('about', views.about, name='about'),
     path('register', views.register_user, name='register'),
     path('login', views.login_user, name='login'),
     path('logout', views.logout_user, name='logout'),
     path('products/phones/<brand>', views.phones_brand, name='phones_by_brand'),
     path('products/phones', views.phones, name='smartphones'),
     path('products/', views.products)
]