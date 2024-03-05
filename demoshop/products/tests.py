from django.test import TestCase
from .models import Brand, SmartWatch


class TestSmartWatch(TestCase):
    def setUp(self):
        Brand.objects.create(name='Apple', description='Apple description')
        Brand.objects.create(name='Samsung', description='Samsung description')

        self.apple_brand = Brand.objects.get(name='Apple')
        self.samsung_brand = Brand.objects.get(name='Samsung')

        self.galaxy_watch = {
            'model': 'Galaxy Watch5',
            'description': 'abc',
            'brand_id': self.samsung_brand,
            'color': 'black',
            'strap_color': 'black',
            'quantity': 50,
            'price': 20999
        }

        self.apple_watch = {
            'model': 'Watch SE',
            'description': 'abc',
            'brand_id': self.apple_brand,
            'color': 'silver',
            'strap_color': 'white',
            'quantity': 25,
            'price': 25499
        }

    def test_negative_quantity(self):
        self.galaxy_watch['quantity'] = -25
        SmartWatch.objects.create(**self.galaxy_watch)
        galaxy = SmartWatch.objects.get(model='Galaxy Watch5')
        galaxy.clean()
        # self.assertGreater(galaxy.quantity, 0)

    def test_negative_price(self):
        self.apple_watch['price'] = -100
        SmartWatch.objects.create(**self.apple_watch)
        apple = SmartWatch.objects.get(model='Watch SE')
        apple.clean()
        # self.assertGreater(apple.price, 0)

