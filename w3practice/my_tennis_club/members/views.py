from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    params = {'mymembers':mymembers}
    return render(request,'all_members.html',params)

def details(request,id):
    mymembers = Member.objects.get(id=id)
    params = {'mymembers':mymembers}
    return render(request,'details.html',params)
    
