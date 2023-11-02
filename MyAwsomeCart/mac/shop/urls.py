from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
   path("",index,name="ShopHome"),
   path("about/",about,name="AboutUs"),
   path("contact/",contact,name="ContactUs"),
   path("tracker",tracker,name="TrackingStatus"),
   path("search",search,name="Search"),
   path("productView/<int:myid>", productView, name="ProductView"),
   path("checkout",checkout,name="Checkout"),
   
]
