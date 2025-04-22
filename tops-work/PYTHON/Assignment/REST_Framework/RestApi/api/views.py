from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializer import *

# Create your views here.
@api_view(['post'])
def addstudents(request):
    ser = StudentSerializer(data=request.data)
    if not ser.is_valid():
        return Response({'status':'202','errors':ser.errors,'message':"something went wrong"})
    ser.save()
    return Response({'status':'200','message':"data added successfully"})

@api_view(['get'])
def viewstudents(request):
    allstudents = Student.objects.all()
    s_data = StudentSerializer(allstudents,many=True)
    print(s_data)
    return Response(data=s_data.data)

@api_view(['put'])
def updatestudents(request,id):
    try:
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,request.data)
        if not ser.is_valid():
            return Response({'status':'202','errors':ser.errors,'message':"something went wrong"})
        ser.save()
        return Response({'status':'200',"data":ser.data,'message':"Stduent updated successfully"})
    
    except Exception as e:
        return Response({'status':"404",'message':'Student Not found'})

@api_view(['delete'])
def deletestudents(request,id):
    try:
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'status':"200",'message':'Student deleted successfully'})
    
    except Exception as e:
        return Response({'status':"404",'message':'Student Not found'})
    

@api_view(['patch'])
def updatesinglestudent(request,id):
        try:
            student = Student.objects.get(pk=id)
            ser =  StudentSerializer(student,request.data,partial=True)
            if not ser.is_valid():
                return Response({'status':'202','errors':ser.errors,'message':"something went wrong"})
            ser.save()
            return Response({'status':'200',"data":ser.data,'message':"Stduent updated successfully"})

        except Exception as e:
            return Response({'status':"404",'message':'Student Not found'})
    
