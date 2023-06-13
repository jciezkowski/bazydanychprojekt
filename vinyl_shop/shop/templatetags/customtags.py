from django import template
from shop.models import Vinyls, Deliveries, Sales
from django.db.models import Sum

register = template.Library()

@register.filter
def get_units(vinyl):
    vid = vinyl.vinylid
    unitsDelivered = Deliveries.objects.filter(vinylid=vid).aggregate(total=Sum('unitsdelivered'))['total']
    if unitsDelivered is None:
        unitsDelivered = 0
    unitsSold = Sales.objects.filter(vinylid=vid).aggregate(total=Sum('quantity'))['total']
    if unitsSold is None:
        unitsSold = 0
    return unitsDelivered - unitsSold