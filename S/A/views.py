from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def login_page(request):
    student_list = Student.objects.all()
    student_dict = {'student_list':student_list}
    return render(request,'login.html',context = student_dict)




def logout_page(request):
    return HttpResponse('<h1><a href="https://www.w3schools.com/bootstrap4/bootstrap_tables.asp">Hello</a></h1>')