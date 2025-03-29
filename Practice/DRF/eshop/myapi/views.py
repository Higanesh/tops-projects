from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapi.models import *
from myapi.serializer import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(["post"])
def registerUser(request):
    data = UserSerializer(data=request.data)
    if not data.is_valid():
            return Response({"status":"202","Errors":data.errors,"message":"something went wrong"})
    data.save()
    
    return Response({"message":"Data Inserted","data":data.data})

class CategoryAPI(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]



    def get(self, request):
        
        allCategories = Category.objects.all()
        data = CategorySerializer(allCategories,many=True)
        return Response(data.data)
    
    def post(self, request):
        data = CategorySerializer(data=request.data)
        if not data.is_valid():
            return Response({"status":"202","Errors":data.errors,"message":"something went wrong"})
        data.save()
        return Response({"message":"Data Inserted","data":data.data})
    
    def put(self, request):
        dataToUpdate = Category.objects.get(pk=request.data['id'])
        updatedData = CategorySerializer(dataToUpdate,request.data)
        if not updatedData.is_valid():
              return Response({"status":"202","Errors":updatedData.errors,"message":"something went wrong"})
        updatedData.save()
        return Response({"message":"Data Updated","data":updatedData.data})
    
    def delete(self, request):
        try :
            dataTodelete = Category.objects.get(pk=request.data['id'])
            dataTodelete.delete()
            return Response({"message":"Data Deleted"})
        except Exception as e:
            return Response({"mesaage":str(e)})
        

# @api_view(['post'])
# def addcategory(request):
#     try:
#         category = CategorySerializer(data = request.data)
#         if not category.is_valid():
#             return Response({'status':'202','message':'Something wrong!','errors':category.errors})
#         category.save()
#         return Response({'status':'200','message':'Category added successfully !'})

#     except Exception as e:
#         return Response({'message':'Something went wrong'})

# @api_view(['get'])
# def viewcategory(request):
#     allcategory = Category.objects.all()
#     c_data = CategorySerializer(allcategory,many=True)
#     return Response(data=c_data.data)

# @api_view(['put'])
# def updatecategory(request,id):
#     try:
#         category = Category.objects.get(pk=id)
#         c_data = CategorySerializer(category,request.data)
#         if not c_data.is_valid():
#             return Response({'status':'202','message':'Something wrong!','errors':c_data.errors})
#         c_data.save()
#         return Response({'status':'200','message':'Category updated successfully !'})

#     except Exception as e:
#         return Response({'message':'Something went wrong'})

# @api_view(['delete'])
# def deletecategory(request,id):
#     try:
#         category = Category.objects.get(pk=id)
#         category.delete()
#         return Response({'status':"200",'message':'Category deleted successfully'})

#     except Exception as e:
#         return Response({'status':"404",'message':'Category Not found'})

@api_view(['post'])
def addproduct(request):
    try:
        product = ProductSerializer(data = request.data)
        if not product.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':product.errors})
        product.save()
        return Response({'status':'200','message':'Product added successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['get'])
def viewproduct(request):
    allproduct = Product.objects.all()
    p_data = ProductSerializer(allproduct,many=True)
    return Response(data=p_data.data)

@api_view(['put'])
def updateproduct(request,id):
    try:
        product = Product.objects.get(pk=id)
        p_data = ProductSerializer(product,request.data)
        if not p_data.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':p_data.errors})
        p_data.save()
        return Response({'status':'200','message':'Product updated successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['delete'])
def deleteproduct(request,id):
    try:
        product = Product.objects.get(pk=id)
        product.delete()
        return Response({'status':"200",'message':'Product deleted successfully'})

    except Exception as e:
        return Response({'status':"404",'message':'Product Not found'})

@api_view(['post'])
def addtocart(request):
    try:
        cart = CartSerializer(data = request.data)
        if not cart.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':cart.errors})
        cart.save()
        return Response({'status':'200','message':'Cart added successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['get'])
def viewcart(request):
    allcart = Cart.objects.all()
    cart_data = CartSerializer(allcart,many=True)
    return Response(data=cart_data.data)

@api_view(['put'])
def updatecart(request):
    try:
        cart = Cart.objects.get(pk=id)
        cart_data = CartSerializer(cart,request.data)
        if not cart_data.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':cart_data.errors})
        cart_data.save()
        return Response({'status':'200','message':'Cart updated successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['delete'])
def deletecart(request,id):
    try:
        cart = Cart.objects.get(pk=id)
        cart.delete()
        return Response({'status':"200",'message':'Cart deleted successfully'})

    except Exception as e:
        return Response({'status':"404",'message':'Cart Not found'})

@api_view(['post'])
def addorder(request):
    try:
        order = OrderSerializer(data = request.data)
        if not order.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':order.errors})
        order.save()
        return Response({'status':'200','message':'Order added successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['get'])
def vieworder(request):
    allorder = Order.objects.all()
    o_data = OrderSerializer(allorder,many=True)
    return Response(data=o_data.data)

@api_view(['put'])
def updateorder(request):
    try:
        order = Order.objects.get(pk=id)
        o_data = OrderSerializer(order,request.data)
        if not o_data.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':o_data.errors})
        o_data.save()
        return Response({'status':'200','message':'Order updated successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})
    
@api_view(['delete'])
def deleteorder(request,id):
    try:
        order = Order.objects.get(pk=id)
        order.delete()
        return Response({'status':"200",'message':'Order deleted successfully'})

    except Exception as e:
        return Response({'status':"404",'message':'Order Not found'})

@api_view(['post'])
def addorderitems(request):
    try:
        orderitems = CartSerializer(data = request.data)
        if not orderitems.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':orderitems.errors})
        orderitems.save()
        return Response({'status':'200','message':'Order Items added successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['get'])
def vieworderitems(request):
    allorderitems = OrderItems.objects.all()
    items_data = OrderItemSerializer(allorderitems,many=True)
    return Response(data=items_data.data)

@api_view(['put'])
def updateorderitems(request):
    try:
        orderitems = OrderItems.objects.get(pk=id)
        items_data = CartSerializer(orderitems,request.data)
        if not items_data.is_valid():
            return Response({'status':'202','message':'Something wrong!','errors':items_data.errors})
        items_data.save()
        return Response({'status':'200','message':'Order Items added successfully !'})

    except Exception as e:
        return Response({'message':'Something went wrong'})

@api_view(['delete'])
def deleteorderitems(request):
    try:
        orderitems = OrderItems.objects.get(pk=id)
        orderitems.delete()
        return Response({'status':"200",'message':'Order Items deleted successfully'})

    except Exception as e:
        return Response({'status':"404",'message':'Order Items Not found'})
    

def productbycategory(request,id):
    return HttpResponse("pass")