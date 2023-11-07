from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
   path("",index,name="blogHome"),
   path("blogpost/<int:id>",blogpost, name="blogHome")
]
