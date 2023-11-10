from django.urls import path
from home.views import *

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('search/',search,name='search'),
    path('signup/',handleSignUp,name='handleSignUp'),
    path('login/',handleLogin,name='handleLogin'),
    path('logout/',handleLogOut,name='handleLogOut'),
]
