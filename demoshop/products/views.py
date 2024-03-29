from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Brand, Phone


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Успешно")
            return redirect('smartphones')
        else:
            messages.error(request, "Неправильный логин или пароль")
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})


def user_profile(request, user_id):
    u = User.objects.get(pk=user_id)

    context = {
        'user': u
    }

    if u is not None:
        return render(request, 'profile.html', context)


def product(request, product_id: int):
    product_row = Phone.objects.get(pk=product_id)

    stats = [
        {'name': 'Экран', 'value': str(product_row.display_size) + '"'},
        {'name': 'Процессор', 'value': product_row.cpu},
        {'name': 'Объём внутренней памяти', 'value': str(product_row.memory) + ' Гб'},
        {'name': 'Объём оперативной памяти', 'value': str(product_row.ram) + ' Гб'},
        {'name': 'Цвет', 'value': product_row.color},
    ]

    if product_row.description is not None:
        stats.append({'name': 'Описание', 'value': product_row.description},)


    context = {
        'product_header': f'{product_row.model} {product_row.memory} Гб',
        'image_url': product_row.image.url,
        'product_id': product_row.id,
        'product_stats': stats
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
        'search': 'Все смартфоны',
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