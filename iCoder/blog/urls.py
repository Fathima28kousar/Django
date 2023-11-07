from django.urls import path
from blog.views import *

urlpatterns = [
    path('',bloghome,name='bloghome'),
    path('blogpost/',blogpost,name='blogpost'),
    
]
