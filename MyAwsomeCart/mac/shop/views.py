from django.shortcuts import render
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from PayTm import Checksum



# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    ## params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products,range(1,len(products)),nSlides],[products,range(1,len(products)),nSlides]]
    # products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name,email,phone,desc)
        contact =Contact(name=name,email = email,phone=phone,desc=desc)
        contact.save()
        thank = True
    return render(request,'shop/contact.html',{'thank':thank})

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderId, email = email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def searchMatch(query, item):
    if query in item.product_name or query in item.category:
        return True
    else:
        return False

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/productview.html',{'product':product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('items_Json','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        order = Order(items_json = items_json,name= name,email = email,address = address,city = city, state = state,zip_code=zip_code,phone=phone,amount = amount)
        order.save()
        update = OrderUpdate(order_id = order.order_id,update_desc="Your order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request,'shop/checkout.html')
#         param_dict={

#                 'MID': 'WorldP64425807474247',
#                 'ORDER_ID': str(order.order_id),
#                 'TXN_AMOUNT': str(amount),
#                 'CUST_ID': email,
#                 'INDUSTRY_TYPE_ID': 'Retail',
#                 'WEBSITE': 'WEBSTAGING',
#                 'CHANNEL_ID': 'WEB',
#                 'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlepayment/',

#         }
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         return render(request, 'shop/paytm.html', {'param_dict': param_dict})
#     return render(request, 'shop/checkout.html')


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'shop/paymentstatus.html', {'response': response_dict})