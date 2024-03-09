import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from products.models import Phone
from .cart import Cart


def cart_page(request):
    context = {}
    return render(request, 'cart.html', context)


def cart_add(request):
    cart = Cart(request)

    product_id = json.loads(request.body)['product_id']

    product = get_object_or_404(Phone, id=product_id)

    cart.add(product=product)

    return JsonResponse({'status': 'ok'})


def cart_update(request):
    pass


def cart_delete(request):
    pass
