from django.shortcuts import render,redirect
from shoppingApp.models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog_single(request):
    return render(request,"blog_single.html")

def blog(request):
    return render(request,"blog.html")

@login_required(login_url="login")
def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")

def shop(request):
    return render(request,"shop.html")

def product_details(request):
    return render(request,"product_details.html")


def login_user(request):
    if request.method=="POST":
        username = request.POST['uname']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect(request,"{%url index.html%}")
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def reg(request):
     
    # pattern = "^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]{2,4}$"

    if request.method == "POST":
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        # result = re.match(email,pattern)
        # if result == None:
        #     return render(request,'reg.html',{"err" : "Invalid Email formate !!!"})
        
        # if User.objects.filter(username=username).exists():
        #      return render(request,'reg.html',{"err" : "User alredy exist !!!"})
        
        user = User.objects.create_user(username=username,email=email,password=password)
        # user.set_password(password)
        user.save()
        return redirect(request,'login.html',{"msg" : "Registration successfully !!!"})
    else:
        return render(request,"reg.html")


def userlogout(request):
    logout(request)
    return render(request,'index.html')
