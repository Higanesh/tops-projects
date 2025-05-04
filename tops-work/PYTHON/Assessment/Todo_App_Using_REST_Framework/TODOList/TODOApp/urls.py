from django.urls import path
from TODOApp.views import *

urlpatterns = [
    path("",loginpage,name="login-page"),
    path("logout",logoutpage,name="logout"),
    path("register",register,name="register-page"),
    path("todoapp",todoapp,name="todoapp-page"),
    path("delete_task/<str:name>",delete_task,name="delete_task"),
    path("update_task/<str:name>",update_task,name="update_task")
]
