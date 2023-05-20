from django.http import HttpResponse
from django.template import loader
from .models import Vinyls, Customers
import random

def allVinyls(request):
    vinyls = Vinyls.objects.all().values()
    template = loader.get_template("allVinyls.html")
    context = {
        'vinyls': vinyls,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.

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
        # Create a new Vinyl object with the form data
        vinyl = Vinyls(title=title, artist=artist, genre=genre, description=description, url=url)

        # Save the object to the database
        vinyl.save()
    context = {
        'vinyl': vinyl
    } 
    return HttpResponse(template.render(context, request))