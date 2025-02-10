from django.shortcuts import render,HttpResponse
from googleapp.models import *

# Create your views here.


def home(request):
    # return HttpResponse("this is the home page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def details(request):
    # return HttpResponse("this is services page")
    return render(request,'details.html')

def apply(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        phoneNumber = request.POST.get('phoneno', '')
        address = request.POST.get('address', '')
        gender = request.POST.get('gender', 'Not Specified')
        language = ', '.join(request.POST.getlist('languages', []))  # No default needed; it returns an empty list if not present
        education = request.POST.get('education', 'Not Specified')
        image = request.FILES.get('image')  # Returns None if no file uploaded

        # Save the data to the database
        apply = Apply(
            firstName=firstName,
            lastName=lastName,
            email=email,
            phoneNumber=phoneNumber,
            address=address,
            gender=gender,
            language=language,
            education=education,
            image=image,
        )
        apply.save()

        return HttpResponse("Application submitted successfully!")  # Provide feedback to the user
    return render(request, 'apply.html')


def login(request):
    return render(request,'login.html')

def reg(request):
    return render(request,'reg.html')

