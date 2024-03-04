from django.db import models


# Create your models here.
class Category(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()