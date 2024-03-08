from django.http import request

class Cart:
    def __init__(self, request_: request):
        self.session = request_.session
        cart = self.session.get('session_key')

        if 'session_key' not in request_.session:
            self.session['session_key'] = {}
            cart = {}

        self.cart = cart
