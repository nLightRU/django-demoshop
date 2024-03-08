from django.shortcuts import render


def cart_page(request):
    context = {}
    return render(request, 'cart.html', context)


def cart_add(request):
    pass


def cart_update(request):
    pass


def cart_delete(request):
    pass
