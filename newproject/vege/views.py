from django.shortcuts import render, redirect
from .models import *

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # Check if all required data is provided
        
        Reciepe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )
        return redirect('/receipes/')

    return render(request, 'receipes.html')


