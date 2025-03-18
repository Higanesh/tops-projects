from django.urls import path
from myapi.views import *

urlpatterns = [
    path("addcategory/",addcategory,name="addcategory"),
    path("viewcategory/",viewcategory,name="viewcategory"),
    path("updatecategory/<id>",updatecategory,name="updatecategory"),
    path("deletecategory/<id>",deletecategory,name="deletecategory"),
    path("addproduct/",addproduct,name="addproduct"),
    path("viewproduct/",viewproduct,name="viewproduct"),
    path("updateproduct/<id>",updateproduct,name="updateproduct"),
    path("deleteproduct/<id>",deleteproduct,name="deleteproduct"),
    path("addtocart/",addtocart,name="addtocart"),
    path("viewcart/",viewcart,name="viewcart"),
    path("updatecart/<id>",updatecart,name="updatecart"),
    path("deletecart/<id>",deletecart,name="deletecart"),
    path("addorder/",addorder,name="addorder"),
    path("vieworder/",vieworder,name="vieworder"),
    path("updateorder/<id>",updateorder,name="updateorder"),
    path("deleteorder/<id>",deleteorder,name="deleteorder"),
    path("addorderitems/",addorderitems,name="addorderitems"),
    path("vieworderitems/",vieworderitems,name="vieworderitems"),
    path("updateorderitems/<id>",updateorderitems,name="updateorderitems"),
    path("deleteorderitems/<id>",deleteorderitems,name="deleteorderitems"),
    path("productbycategory/<id>",productbycategory,name="productbycategory"),
]
