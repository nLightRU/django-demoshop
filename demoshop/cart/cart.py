from django.http import request


class Cart:
    def __init__(self, request_: request):
        self.session = request_.session
        cart = self.session.get('session_key')

        if 'session_key' not in request_.session:
            self.session['session_key'] = {}
            cart = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def count(self):
        return len(self.cart.keys())
