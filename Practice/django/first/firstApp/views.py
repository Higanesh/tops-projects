from django.shortcuts import render, redirect, HttpResponse
from firstApp.models import MyUser
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .utils import send_sms

def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url="userLogin")
def index(request):
    alluser = MyUser.objects.all()
    return render(request,'index.html',{"users":alluser})

def addDetails(request):
    if request.method == 'POST':
        # Get data from the form
        id = request.POST['id']
        fname = request.POST['firstname']
        mname = request.POST['middlename']
        lname = request.POST['lastname']

        if id:
            cuser = MyUser.objects.get(pk=id)
            cuser.fname = fname
            cuser.mname = mname
            cuser.lname = lname
            cuser.save()
        else:

            MyUser.objects.create(fname=fname, mname=mname, lname=lname)
        
        return redirect('index')  # Redirect to home page after saving
    

def deleteDetails(request,id):
    user = MyUser.objects.get(pk=id)
    user.delete()
    return redirect('index')

def editDetails(request,id):
    u =  MyUser.objects.get(pk=id)   
    allusers = MyUser.objects.all()
    return render(request,"index.html",{"u":u,"users":allusers})

def userReg(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("pass")

        if User.objects.filter(username = uname).exists():
            messages.add_message(request,messages.ERROR,"Username already exist !!")
            return render(request,"userreg.html")
        
        user = User(username=uname,email=email)
        user.set_password(password)
        user.save()
        messages.add_message(request,messages.SUCCESS,"Registration Successful !!")
    return render(request,'userreg.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("pass")

        user = authenticate(username=username,password=password)
        if user == None:
            messages.add_message(request,messages.ERROR,"Invalid Credentials !!")
            return render(request,"userlogin.html")
        else:
            login(request,user)
            return redirect("index")
    return render(request,'userlogin.html')

def userlogout(request):
    logout(request)
    return render(request,'dashboard.html')
    

def otp(request):
    return render(request,"otp.html")

def sendsms(request):

    if request.method == "POST":
        phone = request.POST.get("phone")
        
    
        if not phone:
            return JsonResponse({"status": "error", "message": "Phone number is required"})
        
        message = "Your OTP is 123456"
        response = send_sms(phone, message)
        return JsonResponse({"status": "success", "response": response})
    
    return JsonResponse({"status": "error", "message": "Invalid request"})

    


    

def email(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message, 'settings.EMAIL_HOST_USER', [email],fail_silently=False)
    return render(request,"email.html")
    



    




