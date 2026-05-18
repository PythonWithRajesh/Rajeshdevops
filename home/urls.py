from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

    path('contact/', views.contact, name='contact'),

    path('icecream/', views.icecream, name='icecream'),

    path('kulfi/', views.kulfi, name='kulfi'),

    path('badamshake/', views.badamshake, name='badamshake'),

    path('faluda/', views.faluda, name='faluda'),

    path('hocco/', views.hocco, name='hocco'),

    path('oreo/', views.oreo, name='oreo'),

    path('mango/', views.mango, name='mango'),

    path('coffe/', views.coffe, name='coffe'),

    path('familypack/', views.familypack, name='familypack'),
]