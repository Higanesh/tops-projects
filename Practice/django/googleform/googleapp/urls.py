from django.contrib import admin
from django.urls import path
from googleapp.views import *

urlpatterns = [

    path('',home, name='home'),
    path('about',about, name='about'),
    path('details',details, name='details'),
    path('apply',apply, name='apply'),  
    path('login/',login,name='login'), 
    path('reg/',reg,name='reg'),
]
