import decimal

from django.http import request


class Cart:
    def __init__(self, request_: request):
        self.session = request_.session
        cart = self.session.get('session_key')

        if 'session_key' not in request_.session:
            cart = {}
            self.session['session_key'] = cart

        self.cart = cart

    def __len__(self):
        return len(self.cart)

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def price(self) -> str:
        amount = decimal.Decimal('0.0')
        products_keys = [p for p in self.cart]
        for key in products_keys:
            amount += decimal.Decimal(self.cart[key]['price'])

        return str(amount)



    def reset(self):
        products_keys = [p for p in self.cart]
        for k in products_keys:
            del self.cart[k]
        self.session.modified = True