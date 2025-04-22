from django.urls import path
from library.views import *

urlpatterns = [
    path("addauthor/",addauthor,name="addauthor"),
    path("viewauthor/",viewauthor,name="viewauthor"),
    path("updateauthor/",updateauthor,name="updateauthor"),
    path("deleteauthor/",deleteauthor,name="deleteauthor"),
    path("addpublication/",addpublication,name="addpublication"),
    path("viewpublication/",viewpublication,name="viewpublication"),
    path("updatepublication/",updatepublication,name="updatepublication"),
    path("deletepublication/",deletepublication,name="deletepublication"),
    path("addbook/",addbook,name="addbook"),
    path("viewbook/",viewbook,name="viewbook"),
    path("updatebook/",updatebook,name="updatebook"),
    path("deletebook/",deletebook,name="deletebook"),
    path("bookbyauthor/<id>",bookbyauthor,name="bookbyauthor"),
    path("bookbypublication/<id>",bookbypublication,name="bookbypublication"),
    path("bookbyauthorandpublication/<str:a_name>/<str:p_name>/",bookbyauthorandpublication,name="bookbyauthorandpublication")
]
