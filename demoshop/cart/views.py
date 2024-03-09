from django.shortcuts import render
from django.http import HttpResponse

from .context_processors import cart


def cart_page(request):
    context = {}
    return render(request, 'cart.html', context)


def cart_add(request):
    c = cart(request)
    return HttpResponse('')


def cart_update(request):
    pass


def cart_delete(request):
    pass
