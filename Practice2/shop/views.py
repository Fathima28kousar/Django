from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from math import ceil


def home(request):
    items = Item.objects.all()
    allItems = []
    catItems = Item.objects.values('category','id')
    n = len(items)
    nSlides = n//4 +(ceil(n/4)+(n//4))
    params = {'no_of_slides':nSlides,'range':range(1,nSlides),'item':items}
    return render(request,'shop/index.html',params)

def about(request):
    return HttpResponse('<h1>this is about page</h1>')

def contact(request):
    return HttpResponse('<h1>this is contact page </h1>')

def tracker(request):
    return HttpResponse('this is tracker page')

def search(request):
    return HttpResponse('this is search page')

def productView(request):
    return HttpResponse('this is productView page')

def checkout(request):
    return HttpResponse('this is checkout page')


