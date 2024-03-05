from django.http import HttpResponse
from .models import Brand, Phone


def index(request):
    return HttpResponse('Hello from products')


def phones_brand(request, brand):
    brand = brand.title()
    chosen_brand = Brand.objects.filter(name=brand)[0]
    phones_rows = Phone.objects.filter(brand_id=chosen_brand.id)
    phones_names = [str(phone) for phone in phones_rows]
    resp = ', '.join(phones_names)
    return HttpResponse(resp)


def phones(request):
    phones_ = Phone.objects.all()
    series = []
    for phone in phones_:
        series.append(phone.series)

    resp = ', '.join(series)
    return HttpResponse(resp)


def products(request):
    phones_rows = Phone.objects.all()
    phones_names = [str(phone) for phone in phones_rows]
    resp = ', '.join(phones_names)
    return HttpResponse(resp)