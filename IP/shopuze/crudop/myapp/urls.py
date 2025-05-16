from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("addemp",addemp,name="addemp"),
    path("updateemp/<int:id>",updateemp,name="updateemp"),
    path("delemp/<int:id>",delemp,name="delemp")
]
