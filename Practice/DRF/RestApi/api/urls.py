from django.urls import path
from api.views import *

urlpatterns = [
    path("addstudents/",addstudents,name="addstudents"),
    path("viewstudents/",viewstudents,name="viewstudents"),
    path("updatestudents/<id>",updatestudents,name="updatestudents"),
    path("deletestudents/<id>",deletestudents,name="deletestudents"),
    path("updatesinglestudent/<id>",updatesinglestudent,name="updatesinglestudent"),
]
