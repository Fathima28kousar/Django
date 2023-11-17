from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from math import ceil


def home(request):
    allProds = []
    catprods = Item.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Item.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params = {'allProds':allProds}

    product = request.POST.get('product')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity + 1
        else:
            cart[product] =1
    else:
        cart ={}
        cart[product] = 1
    request.session['cart'] = cart
    print('cart',request.session['cart'])
    # request.session.get('cart').clear()
    return render(request, 'shop/index.html', params)



    
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


