from django.shortcuts import render,HttpResponse
from myapp.models import *
from myapp.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my Web")

@api_view(['post'])
def addDetails(request):
    user = userSerializer(data=request.data)
    if not user.is_valid():
        return Response({'message':"something went wrong"})
    user.save()
    return Response({'message':"User added successfully"})

@api_view(['get'])
def viewDetails(request):
    alluser = Myuser.objects.all()
    u_data = userSerializer(alluser,many=True)
    return Response(data=u_data.data)

@api_view(['put'])
def updateDetails(request,id):
    try:
        u_data = Myuser.objects.get(pk=id)
        user = userSerializer(u_data,request.data)
        if not user.is_valid():
            return Response({'message':"something went wrong"})
        user.save()
        return Response({'message':"User updated successfully"})
    except Exception as e:
        return Response({'message':"User not found"})
    
@api_view(['delete'])
def deleteDetails(request,id):
    try:
        u_data = Myuser.objects.get(pk=id)
        u_data.delete()
        return Response({'message':"User deleted successfully"})
    except Exception as e:
        return Response({'message':"User not found"})
