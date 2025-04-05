from django.shortcuts import render

# Create your views here.

def addDetails(request):
    return render(request,"index.html")

def viewDetails(request):
    return render(request,"index.html")

def updateDetails(request):
    return render(request,"index.html")

def deleteDetails(request):
    return render(request,"index.html")




