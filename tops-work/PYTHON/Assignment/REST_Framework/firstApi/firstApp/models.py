from django.db import models

# Create your models here.
class Employee(models.Model):
    empName = models.CharField(max_length=20,default="test")
    email = models.CharField(max_length=20,default="test")
    age = models.IntegerField()

