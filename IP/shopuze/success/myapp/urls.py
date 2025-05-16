from django.urls import path
from myapp.views import *

urlpatterns = [
    path('add/',add),
    path('view/',view),
    path('update/<int:id>',update),
    path('delete/<int:id>',deldata),
    path('updateone/<int:id>',updateone),
]
