from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("addDetails",addDetails,name="addDetails"),
    path("updateDetails/<id>",updateDetails,name="updateDetails"),
    path("deleteDetails/<id>",deleteDetails,name="deleteDetails")
]
