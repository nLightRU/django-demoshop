from django.http import HttpResponse
from django.shortcuts import render
from .models import Brand, Phone


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def register_user(request):
    return render(request, 'register.html', {})


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