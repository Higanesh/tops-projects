from django.shortcuts import render,redirect
from shoppingApp.models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
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

@login_required(login_url="login_user")
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
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        
        user = authenticate(username=username,password=password)
        if user == None:
            messages.add_message(request,messages.ERROR,"Invalid Credentials !!")
            return render(request,"login.html")
        else:
            login(request,user)
            return redirect("index")
    return render(request,'login.html')

def reg(request):
     if request.method == 'POST':
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("pass")

        if User.objects.filter(username = uname).exists():
            messages.add_message(request,messages.ERROR,"Username already exist !!")
            return redirect(request,"reg.html")
        
        user = User(username=uname,email=email)
        user.set_password(password)
        user.save()
        messages.add_message(request,messages.SUCCESS,"Registration Successful !!")
        return render(request,'reg.html')
     
     else:
         return render(request,"reg.html")
     





    # pattern = "^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]{2,4}$"

    # if request.method == "POST":
    #     uname = request.POST.get("uname")
    #     email = request.POST.get("email")
    #     password = request.POST.get("pass")

    #     result = re.match(email,pattern)
    #     if result == None:
    #         return render(request,'reg.html',{"err" : "Invalid Email formate !!!"})
        
    #     if User.objects.filter(username=uname).exists():
    #          return render(request,'reg.html',{"err" : "User alredy exist !!!"})
        
    #     user = User.objects.create_user(username=uname,email=email)
    #     user.set_password(password)
    #     user.save()
    #     return redirect(request,'login.html',{"msg" : "Registration successful !!!"})
    # else:
    #     return render(request,"reg.html")


def userlogout(request):
    logout(request)
    return render(request,'index.html')





