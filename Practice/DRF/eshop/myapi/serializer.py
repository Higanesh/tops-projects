from rest_framework import serializers
from myapi.models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'

        def create(self, data):
            user = User.objects.create(username=data['username'])
            user.set_password(data['password'])
            user.save()
            Token.objects.create(user=user)
            return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'
    
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category'] = CategorySerializer(instance.category).data
        return resp

class CartSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cart
        fields = '__all__'
    
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['user'] = User(instance.user).data
        resp['product'] = Product(instance.product).data
        return resp

class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Order
        fields = '__all__'
    
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['user'] = User(instance.user).data
        return resp

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = OrderItems
        fields = '__all__'
    
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['order'] = Order(instance.order).data
        resp['product'] = Product(instance.product).data
        return resp