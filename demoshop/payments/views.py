import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

from yookassa import Payment
from yookassa import Configuration

from demoshop import settings
from cart.cart import Cart


def create_payment(request):
    if request.method == 'POST':
        Configuration.account_id = settings.YOOKASSA_SHOP_ID
        Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

        idempotence_key = str(uuid.uuid4())
        order_price = Cart(request).price()

        payment = Payment.create({
            "amount": {
                "value": order_price,
                "currency": "RUB"
            },
            "payment_method_data": {
                "type": "bank_card"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "localhost:8000/"
            },
            "description": "Test payment"
            },
            idempotence_key
        )

        payment_resp = {
            "id": payment["id"],
            "status": payment["status"],
            "confirmation_url": payment["confirmation"]["confirmation_url"]
        }

        return redirect(payment_resp["confirmation_url"])


def payment_succsess(request):
    return HttpResponse('')