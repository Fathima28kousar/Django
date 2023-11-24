from django.urls import path
from members.views import *

urlpatterns = [
    path('', members, name='members'),
    path('details/<int:id>',details,name='details'),
]
