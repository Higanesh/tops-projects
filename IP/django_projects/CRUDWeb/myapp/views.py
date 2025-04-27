from django.shortcuts import render,HttpResponse,redirect
from myapp.models import *

# Create your views here.

def index(request):
    alluser = Myuser.objects.all()
    return render(request,"index.html",{"user":alluser})

def addDetails(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        city = request.POST.get('city')

        if id:
            cuser = Myuser.objects.get(pk=id)
            cuser.name = name
            cuser.age = age
            cuser.email = email
            cuser.city = city
            cuser.save()
        else:
            Myuser.objects.create(name=name, age=age, email=email, city=city)
    return redirect('index')

def updateDetails(request,id):
    ud = Myuser.objects.get(pk=id)
    updateduser = Myuser.objects.all()
    return render(request,"index.html",{"ud":ud,"user":updateduser})

def deleteDetails(request,id):
    dd = Myuser.objects.get(pk=id)
    dd.delete()
    return redirect('index')




