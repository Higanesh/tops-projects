from django.shortcuts import render
from myapp.models import *
from myapp.ser import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['post'])
def add(request):
    deta = NameSer(data=request.data)
    if not deta.is_valid():
        return Response({'message':"wrong"})
    deta.save()
    return Response({'message':"added"})

@api_view(['get'])
def view(request):
    alldata = Name.objects.all()
    v_data = NameSer(alldata,many=True)
    return Response(data=v_data.data)

@api_view(['put'])
def update(request,id):
    d = Name.objects.get(pk=id)
    u = NameSer(d,request.data)
    if not u.is_valid():
        return Response({'message':"wrong"})
    u.save()
    return Response({'message':"updated"})

@api_view(['get','delete'])
def deldata(request,id):
    d = Name.objects.get(pk=id)
    d.delete()
    return Response({'message':"deleted"})

@api_view(['patch'])
def updateone(request,id):
    d = Name.objects.get(pk=id)
    u = NameSer(d,request.data,partial=True)
    if not u.is_valid():
        return Response({'message':"wrong"})
    u.save()
    return Response({'message':"updated"})