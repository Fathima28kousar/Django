from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='About us'),
    path('contact/',contact,name='Contact us'),
    path('tracker/',tracker,name='tracker'),
    path('search/',search,name='search'),
    path('productView/',productView,name='productView'),
    path('checkout/',checkout,name='checkout'),
    path('cart/',cart,name='cart'),
]
