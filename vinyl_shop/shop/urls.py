from django.urls import path
from . import views

urlpatterns = [
    path('vinyls/', views.shop, name='shop'),
    path('clients/', views.clients, name='clients'),
]