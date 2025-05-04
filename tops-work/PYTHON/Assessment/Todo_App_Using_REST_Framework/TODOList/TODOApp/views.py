from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from TODOApp.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("todoapp-page")
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('todoapp-page')
        else:
            messages.error(request,"Wrong user details or User does not exists!")
            return redirect('login-page')
    return render(request,"login.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("todoapp-page")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if len(password) < 4 :
            messages.error(request,"Password must be atleast 4 characters")
            return redirect('register-page')
        
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,"User already exists!")
            return redirect('register-page')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request,"User register successfully")
    return render(request,"register.html")

@login_required
def todoapp(request):
    if request.method == "POST":
        task = request.POST.get("task")
        new_todo = todo(user=request.user,todo_name=task)
        new_todo.save()

    alltodos = todo.objects.filter(user=request.user)
    context = {
        'todos' : alltodos
    }
    return render(request,"todoapp.html", context)

@login_required
def delete_task(request,name):
    get_todo = todo.objects.get(user=request.user,todo_name=name)
    get_todo.delete()
    return redirect('todoapp-page')

@login_required
def update_task(request,name):
    get_todo = todo.objects.get(user=request.user,todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('todoapp-page')

def logoutpage(request):
    logout(request)
    return redirect("login-page")