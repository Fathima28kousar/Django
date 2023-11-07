from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bloghome(request):
    return render(request,'blog/bloghome.html')

def blogpost(request):
    return render(request,'blog/blogpost.html')