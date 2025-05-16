from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    allemp = Employee.objects.all()
    return render(request,"index.html",{"emps":allemp})

def addemp(request):
    if request.method=='POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        
        if(id):
            currentemp = Employee.objects.get(pk=id)
            currentemp.name = name
            currentemp.age = age
            currentemp.email = email
            if request.FILES.get('img'):
                currentemp.img = request.FILES['img'] 
            currentemp.save()
        else:
            Employee.objects.create(name=name, age=age, email=email, img=img)
    return redirect('index')
    
def updateemp(request,id):
    editemp = Employee.objects.get(pk=id)
    allemp = Employee.objects.all()
    return render(request,'index.html',{"editemp":editemp,"emps":allemp})

def delemp(request,id):
    delemp = Employee.objects.get(pk=id)
    delemp.delete()
    return redirect("index")