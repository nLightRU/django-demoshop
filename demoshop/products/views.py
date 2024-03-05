from django.http import HttpResponse
from .models import Brand, Phone


def index(request):
    return HttpResponse('Hello from products')


def phones(request):
    phones_ = Phone.objects.all()
    series = []
    for phone in phones_:
        series.append(phone.series)

    resp = ', '.join(series)
    return HttpResponse(resp)
