from django.urls import path
from myapp.views import *

urlpatterns = [
    path("addemp/",addemp,name="addemp"),
    path("viewemp/",viewemp,name="viewemp"),
    path("updateemp/<id>",updateemp,name="updateemp"),
    path("delemp/<id>",delemp,name="deleteemp"),
]

