from django.shortcuts import render,HttpResponse
from firstApp.models import *

# Create your views here.

def addemp(request):
    return HttpResponse("employee added successfully")

def viewemp(request):
    return HttpResponse("employee viewed successfully")

def updateemp(request):
    return HttpResponse("employee updated successfully")

def deleteemp(request):
    return HttpResponse("employee deleted successfully")