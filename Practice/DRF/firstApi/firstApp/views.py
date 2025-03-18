from django.shortcuts import render,HttpResponse
from firstApp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstApp.serializer import *

# Create your views here.
@api_view(['post'])
def addemp(request):
    empData = EmployeeSerializer(data=request.data)
    if not empData.is_valid():
        return Response({'status':'202','errors':empData.errors,'message':"something went wrong"})
    empData.save()
    return Response({'message':"Employee added successfully"})

@api_view(['get'])
def viewemp(request):
    allemployee = Employee.objects.all()
    e_data = EmployeeSerializer(allemployee,many=True)
    print(e_data)
    return Response(data=e_data.data)

@api_view(['put'])
def updateemp(request,id):
    try:
        employee = Employee.objects.get(pk=id)
        empData = EmployeeSerializer(employee,request.data)
        if not empData.is_valid():
            return Response({'status':'202','errors':empData.errors,'message':"something went wrong"})
        empData.save()
        return Response({'status':'200',"data":empData.data,'message':"Employee updated successfully"})
    except Exception as e:
        return Response({'status':"404",'message':'Employee Not found'})
    

@api_view(['delete'])
def deleteemp(request,id):
    try:
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return Response({'status':"200",'message':'Employee deleted successfully'})
    
    except Exception as e:
        return Response({'status':"404",'message':'Employee Not found'})
    
@api_view(['patch'])
def updatesingleemp(request,id):
    try:
        employee = Employee.objects.get(pk=id)
        empData = EmployeeSerializer(employee,request.data,partial=True)
        if not empData.is_valid():
            return Response({'status':'202','errors':empData.errors,'message':"something went wrong"})
        empData.save()
        return Response({'status':'200',"data":empData.data,'message':"Employee updated successfully"})
    except Exception as e:
        return Response({'status':"404",'message':'Employee Not found'})
    
    
    