from django.shortcuts import render
from crudapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def adduser(request):
    if request.method=='POST':
        uname = request.POST['uname']
        email= request.POST['email']
        phone=request.POST['phone']

        adduser.objects.create(username=uname,email=email,phone=phone)
    
    return render(request,"index.html",{"msg":"Registration successful"})