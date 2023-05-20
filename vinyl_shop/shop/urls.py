from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('vinyls/', views.allVinyls, name='allVinyls'),
    path('clients/', views.clients, name='clients'),
    path('', views.mainPage, name='mainPage'),
    path('adminPanel', views.adminPanel, name='adminPanel'),
    path('addVinyl/', views.addVinyl, name='addVinyl'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)