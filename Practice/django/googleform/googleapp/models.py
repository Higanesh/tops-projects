from django.db import models

# Create your models here.
class Apply(models.Model):
    firstName = models.CharField(max_length=122)
    lastName = models.CharField(max_length=122)
    email = models.EmailField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=122)
    gender = models.CharField(max_length=10,null=True)
    language = models.CharField(max_length=50,null=True)
    education = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='image',null=True)
    
