from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("<h1> contact us page </h1>")

def tracker(request):
    return HttpResponse("<h1> tracker page </h1>")

def search(request):
    return HttpResponse("<h1> search page </h1>")

def productView(request):
    return HttpResponse("<h1> productView page </h1>")

def checkout(request):
    return HttpResponse("<h1> checkout page </h1>")