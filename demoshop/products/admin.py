from django.contrib import admin

from .models import Brand, Phone, SmartWatch

admin.site.register(Brand)
admin.site.register(Phone)
admin.site.register(SmartWatch)