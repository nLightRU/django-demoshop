from django.db import models
from django.core.exceptions import ValidationError


class Brand(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    model = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True, default='', null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/phone/', null=True)

    display_size = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    cpu = models.CharField(blank=True, null=True)
    memory = models.IntegerField(default=64)
    ram = models.IntegerField(default=4)
    color = models.CharField(max_length=20, default='black')

    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=200000.00)

    def clean(self):
        if self.quantity < 0:
            raise ValidationError("Amount can't be negative")
        elif self.price < 0:
            raise ValidationError("Price can't be negative")
        elif self.memory < 0:
            raise ValidationError("Memory can't be negative")

    def __str__(self) -> str:
        return f'{self.model} {self.memory} Gb {self.color.title()}'
