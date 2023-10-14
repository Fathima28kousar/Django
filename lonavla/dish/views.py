from django.shortcuts import render,redirect
from .models import *

def dish(request):
    if request.method=='POST':
        data=request.POST
        dish_name = data.get('dish_name')
        dish_description = data.get('dish_description')
        dish_image = request.FILES.get('dish_image')

        Dish.objects.create(
            dish_name = dish_name,
            dish_description = dish_description,
            dish_image = dish_image,
        )

        return redirect('/dish/')
    queryset = Dish.objects.all()
    context = {'dish':queryset}

    return render(request,'dish.html',context)
