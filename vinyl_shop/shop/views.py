from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q, Sum, ExpressionWrapper, IntegerField,F
from .models import Vinyls, Customers,Sales, Deliveries
from django.db.models.functions import Coalesce
from django.db.models.functions import Lower
from itertools import chain
import operator
from datetime import date

import random

def allVinyls(request):
    vinyls = Vinyls.objects.none()
    if request.method == 'GET':
        genres = request.GET.getlist('genres')
        if genres:
            for mygenre in genres:
                vinyls = chain(vinyls, Vinyls.objects.filter(genre=mygenre))
        else:
            vinyls = chain(vinyls, Vinyls.objects.all())
        sort_method = request.GET.get('sort')
        if sort_method:
            if sort_method == "price_desc":
                vinyls = sorted(vinyls, key=operator.attrgetter('price'), reverse=True)        
            elif sort_method == "price_asc":
                vinyls = sorted(vinyls, key=operator.attrgetter('price'))
            elif sort_method == "title":
                get_key = operator.attrgetter('title')
                vinyls = sorted(vinyls, key=lambda x: get_key(x).lower())
            elif sort_method == "artist":
                get_key = operator.attrgetter('artist')
                vinyls = sorted(vinyls, key=lambda x: get_key(x).lower())
    template = loader.get_template("allVinyls.html")
    context = {
        'vinyls': vinyls,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.

def search(request):
    if request.method == 'POST':
        search_query = request.POST['searchbar']
        posts = Vinyls.objects.filter(Q(title__icontains=search_query) | Q(artist__icontains=search_query) | Q(genre__icontains=search_query) | Q(description__icontains=search_query))
        return render(request, 'search.html', {'query':search_query, 'posts': posts})
    else:
        return render(request, 'search.html', {})

def clients(request):
    allCustomers = Customers.objects.all().values()
    template = loader.get_template("allCustomers.html")
    context = {
        'allCustomers': allCustomers,
    }
    return HttpResponse(template.render(context,request))

def mainPage(request):
    template = loader.get_template("main.html")
    
    mainVinyls = Vinyls.objects.all().values()
    if len(mainVinyls) > 4:
        mainVinyls = random.sample(list(mainVinyls), 4)
    context = {
        'mainVinyls': mainVinyls,
    }
    return HttpResponse(template.render(context, request))

def adminPanel(request):
    template = loader.get_template("adminPanel.html")
    context = {}
    return HttpResponse(template.render(context, request))

def salesStats(request):
    template = loader.get_template("salesStats.html")
    queryset = Vinyls.objects.annotate(
        sprzedane=Coalesce(Sum('sales__quantity'), 0),
        total_price=ExpressionWrapper(
            Coalesce(Sum('sales__quantity') * F('price'), 0),
            output_field=IntegerField()
        )
    ).order_by('-total_price')
    context = {
        'stats': queryset,
    }
    return HttpResponse(template.render(context, request))
def addVinyl(request):
    template = loader.get_template("addVinyl.html")
    vinyl = None
    if request.method == 'GET':
        # Retrieve the form data from the request.POST dictionary
        title = request.GET.get('title')
        artist = request.GET.get('artist')
        genre = request.GET.get('genre')
        description = request.GET.get('description')
        url = request.GET.get('url')
        price = request.GET.get('price')
        # Create a new Vinyl object with the form data
        if '' not in [title, artist, genre, description, url,price]:
            vinyl = Vinyls(title=title, artist=artist, genre=genre, description=description, url=url, price=price)
            vinyl.save()
            context = {
                'vinyl': vinyl
            } 
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse(template.render({}, request))

def addDelivery(request):
    template = loader.get_template("addDelivery.html")
    vinyl = None
    if request.method == 'GET':
        # Retrieve the form data from the request.POST dictionary
        title = request.GET.get('title')
        artist = request.GET.get('artist')
        units = request.GET.get('units')
        vinyl = Vinyls.objects.filter(Q(title=title) & Q(artist=artist)).first()
        if vinyl:
            newdate = date.today()
            delivery = Deliveries(dateofdelivery=newdate, vinylid=vinyl, unitsdelivered=units)
            delivery.save()
        else:
            delivery = None
    context = {
        'delivery': delivery,
        'vinyl': vinyl
    } 
    return HttpResponse(template.render(context, request))