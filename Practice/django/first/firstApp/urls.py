from django.urls import path
from firstApp.views import *

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('index', index, name="index"),  
    path('addDetails', addDetails, name="addDetails"),
    path('deleteDetails/<id>',deleteDetails,name="deleteDetails"),
    path('editDetails/<id>',editDetails,name="editDetails"),
    path('userreg',userReg,name="userReg"),
    path('userlogin',userLogin,name="userLogin"),
    path('userlogout',userlogout,name="userlogout"),
    path('otp',otp,name="otp"),
    path('sendsms',sendsms,name="sendsms"),
    path('email',email,name="email"),
    # path('send_mail_page',send_mail_page,name="send_mail_page"),
]
