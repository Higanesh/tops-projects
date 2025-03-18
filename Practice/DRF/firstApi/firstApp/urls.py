from django.urls import path
from firstApp.views import *

urlpatterns = [
    path("addemp/",addemp,name="addemp"),
    path("viewemp/",viewemp,name="viewemp"),
    path("updateemp/<id>",updateemp,name="updateemp"),
    path("deleteemp/<id>",deleteemp,name="deleteemp"),
    path("updatesingleemp/<id>",updatesingleemp,name="updatesingleemp"),
]
