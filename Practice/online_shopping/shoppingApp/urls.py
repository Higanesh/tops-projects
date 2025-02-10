from django.contrib import admin
from django.urls import path
from shoppingApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',index,name='index'),
    path('about',about,name='about'),
    path('blog_single',blog_single,name='blog_single'),
    path('blog',blog,name='blog'),
    path('cart',cart,name='cart'),
    path('checkout',checkout,name='checkout'),
    path('contact',contact,name='contact'),
    path('shop',shop,name='shop'),
    path('product_details',product_details,name='product_details'),
    path('login_user',login_user,name='login_user'),
    path('reg',reg,name='reg'),
    path("logout",userlogout,name="logout"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)