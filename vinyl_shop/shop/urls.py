from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('vinyls/', views.allVinyls, name='allVinyls'),
    path('', views.mainPage, name='mainPage'),
    path('adminPanel', views.adminPanel, name='adminPanel'),
    path('addVinyl/', views.addVinyl, name='addVinyl'),
    path('addDelivery/', views.addDelivery, name='addDelivery'),
    path('search/', views.search, name='search'),
    path('salesStats/', views.salesStats, name='salesStats'),
    path('basket/', views.basket, name='basket'),
    path('purchased/', views.purchased, name='purchased')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)