from django.shortcuts import render
from library.models import *
from library.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def addauthor(request):
    try:
        author = AuthorSerializer(data = request.data)
        if not author.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':author.errors})
        author.save()
        return Response({'status':'200','message':'Author inserted !','errors':author.data})
    
    except Exception as e:
        return Response({'message':'Something went wrong'})
    
@api_view(['GET'])
def viewauthor(request):
    allauthor = Author.objects.all()
    a_data = AuthorSerializer(allauthor,many=True)
    return Response(data=a_data.data)

def updateauthor(request):
    pass

def deleteauthor(request):
    pass

@api_view(['post'])
def addpublication(request):
    try:
        publication = PublicationSerializer(data = request.data)
        if not publication.is_valid():
            return Response({'status':'202','message':'Something went wrong!','errors':publication.errors})
        publication.save()
        return Response({'status':'200','message':'Publication inserted !','errors':publication.data})
    
    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['get'])
def viewpublication(request):
    allpublication = Publication.objects.all()
    p_data = PublicationSerializer(allpublication,many=True)
    return Response(data=p_data.data)

def updatepublication(request):
    pass

def deletepublication(request):
    pass

@api_view(['post'])
def addbook(request):
    try:
        book = BookSerializer(data = request.data)
        if not book.is_valid():
            return Response({'status':'202','message':'Something went wrong!','errors':book.errors})
        book.save()
        return Response({'status':'200','message':'Publication inserted !','errors':book.data})
    
    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['get'])
def viewbook(request):
    allbooks = Book.objects.all()
    b_data = BookSerializer(allbooks,many=True)
    return Response(data=b_data.data)
    
def updatebook(request):
    pass

def deletebook(request):
    pass

@api_view(['get'])
def bookbyauthor(request,id):
    books = Book.objects.filter(author=id)
    b_data = BookSerializer(books,many=True)
    return Response(data=b_data.data)
    
@api_view(['get'])
def bookbypublication(request,id):
    books = Book.objects.filter(publication=id)
    b_data = BookSerializer(books,many=True)
    return Response(data=b_data.data)

@api_view(['get'])
def bookbyauthorandpublication(request,a_name,p_name):
    books = Book.objects.filter(author__authorName=a_name, publication__publicationName=p_name)
    b_data = BookSerializer(books,many=True)
    return Response(data=b_data.data)


