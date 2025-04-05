from django.urls import path

urlpatterns = [
    path("addDetails",addDetails,name="addDetails"),
    path("viewDetails",viewDetails,name="viewDetails"),
    path("updateDetails",updateDetails,name="updateDetails"),
    path("deleteDetails",deleteDetails,name="deleteDetails")
]
