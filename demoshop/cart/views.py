import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from products.models import Phone
from .cart import Cart


def cart_page(request):
    context = {
        'cart': Cart(request).cart,
        'products': None,
        'total_price': 0,
    }

    products = [Phone.objects.get(pk=key) for key in context['cart']]
    if len(products) != 0:
        context['products'] = products
        for p in products:
            context['total_price'] += p.price

    return render(request, 'cart.html', context)


def cart_add(request):
    cart = Cart(request)

    product_id = json.loads(request.body)['product_id']

    product = get_object_or_404(Phone, id=product_id)

    cart.add(product=product)

    return JsonResponse({'cart_count': cart.count()})


def cart_update(request):
    pass


def cart_delete(request):
    pass


def cart_reset(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart.reset()

        return redirect('/cart')
