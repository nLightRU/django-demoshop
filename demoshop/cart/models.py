from django.db import models
from django.contrib.auth.models import User
from products.models import Phone


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_sum = models.DecimalField(max_digits=12, decimal_places=2)

class OrderPostion(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

