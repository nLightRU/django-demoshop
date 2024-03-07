from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Brand, Phone


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Успешно")
            return redirect('home')
        else:
            messages.error(request, "Неправильный логин или пароль")
            return redirect('home')

    else:
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})


def product(request, product_id: int):
    product_row = Phone.objects.get(pk=product_id)

    context = {
        'product_header': f'{product_row.series} {product_row.model}'
    }

    return render(request, 'product.html', context)

def phones_brand(request, brand):
    brand = brand.title()
    chosen_brand = Brand.objects.filter(name=brand)[0]
    phones_rows = Phone.objects.filter(brand_id=chosen_brand.id)

    context = {
        'search': f'Смартфоны {brand}',
        'results': phones_rows
    }

    return render(request, 'search_template.html', context)


def phones(request):
    phones_rows = Phone.objects.all()

    context = {
        'search': 'Смартфоны',
        'results': phones_rows
    }

    return render(request, 'search_template.html', context)


def products(request):
    phones_rows = Phone.objects.all()

    context = {
        'search': 'Смартфоны',
        'results': phones_rows
    }

    return render(request, 'search_template.html', context)