from django.contrib import admin
from django.urls import path,include
from studentapp.views import *
urlpatterns = [
    path("",index,name="index"),
    path("marks/<id>",marks,name="marks")
]