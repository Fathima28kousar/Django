from django.contrib import admin
from django.urls import path
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("",index,name="ShopHome"),
   path("about/",about,name="AboutUs"),
   path("contact/",contact,name="ContactUs"),
   path("tracker",tracker,name="TrackingStatus"),
   path("search",search,name="Search"),
   path("productView",productView,name="Productview"),
   path("checkout",checkout,name="Checkout"),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
