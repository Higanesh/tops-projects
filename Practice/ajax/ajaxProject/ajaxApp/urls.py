
from django.contrib import admin
from django.urls import path,include
from ajaxApp.views import *

urlpatterns = [
    path('', index, name="index.html"),
    path("addstudent",addstudent,name="addstudent"),
    path("viewstudent",viewstudent,name="viewstudent"),
]
