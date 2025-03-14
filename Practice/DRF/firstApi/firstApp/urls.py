from django.urls import path
from firstApp.views import *

urlpatterns = [
    path("addemp/",addemp,name="addemp"),
    path("viewemp/",viewemp,name="viewemp"),
    path("updateemp/",updateemp,name="updateemp"),
    path("deleteemp",deleteemp,name="deleteemp"),
]
