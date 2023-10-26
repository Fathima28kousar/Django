from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *


def login_page(request):
    student_list = Student.objects.all()
    student_dict = {'student_list':student_list}
    return render(request,'login.html',context = student_dict)

def home(request):

    return HttpResponse("""<h1 style="background-color:red">Good morning</h1>
                        <h1 class="container">vegetables page</h1>
                        <p class="container"><a href="/">home | </a>
                        <a href="/login_page/">login_page | </a>
                        <a href="/logout_page/">logout_page | </a>
                        <a href="/house/">house | </a></p>""")

def house(request):
    
    peoples = [
        {'name':'fathima','age':24,'location':'london'},
        {'name':'fathima','age':24,'location':'london'},
        {'name':'fathima','age':24,'location':'london'},
        {'name':'fathima','age':24,'location':'london'},
        {'name':'fathima','age':24,'location':'london'},
        {'name':'fathima','age':24,'location':'london'},
    ]

    text = '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, in error voluptate odio illum, rem magni quis nemo at reiciendis facilis laudantium quo praesentium itaque quam voluptates, modi eum maxime.
    Dicta quibusdam vitae officiis rerum! Accusamus voluptatibus harum labore inventore libero ullam similique natus minus earum esse dolore fugit quasi expedita vel soluta explicabo magni laborum cumque, ratione temporibus suscipit.
    Laborum in cum a vitae sint eius possimus magni laboriosam assumenda nam qui, molestiae rerum natus ducimus iure delectus quaerat, cumque commodi quos sit temporibus consectetur unde quod praesentium! Quas?'''

    vegetables = ["tomato","potato","cucumber","coconut","brinjal","onion","banana"]

    return render(request,'index.html',context={'peoples':peoples,'text':text,'vegetables':vegetables})

    

def logout_page(request):
    return HttpResponse('<h1><a href="https://www.w3schools.com/bootstrap4/bootstrap_tables.asp">Hello</a></h1><h1 class="container">vegetables page</h1>')

def car(request):
    if request.method=="POST":
        data = request.POST
        car_name = data.get('car_name')
        car_speed = data.get('car_speed')
        car_price = data.get('car_price')
        car_description = data.get('car_description')
        car_image = request.FILES.get('car_image')

        Car.objects.create(
            car_name = car_name,
            car_speed = car_speed,
            car_price = car_price,
            car_description = car_description,
            car_image = car_image
        )
        return redirect('/car/')
    queryset = Car.objects.all()
    context = {'car':queryset}
    return render(request,'car.html',context)

def delete_car(request,id):
    queryset = Car.objects.get(id = id)
    queryset.delete()

    return redirect('/car/')

def update_car(request,id):
    queryset = Car.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        car_name = data.get('car_name')
        car_price = data.get('car_price')
        car_image = request.FILES.get('car_image')
        queryset.car_name = car_name
        queryset.car_price = car_price
        if car_image :
            queryset.car_image = car_image
            queryset.save()


    context = {'car':queryset}
    return render(request,'update_car.html',context)

def index(request):
    params = {'name':'fathima','place':'Mars'}
    return render(request,'one.html',params)

def removepunc(request):
    djtext = (request.GET.get('text', 'default'))
    print(djtext)
    return HttpResponse("<h1> remove punctuation </h1>")

def ex(request):
    sites = ['''
             <h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>
             <h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>
             <h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>
             <h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>
             ''' ]
            
    return HttpResponse((sites))


