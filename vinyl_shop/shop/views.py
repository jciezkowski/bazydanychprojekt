from django.http import HttpResponse
from django.template import loader
from .models import Vinyls, Clients

def shop(request):
    myvinyls = Vinyls.objects.all().values()
    template = loader.get_template("all_vinyls.html")
    context = {
        'myvinyls': myvinyls,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.

def clients(request):
    allclients = Clients.objects.all().values()
    template = loader.get_template("all_clients.html")
    context = {
        'allclients': allclients,
    }
    return HttpResponse(template.render(context,request))