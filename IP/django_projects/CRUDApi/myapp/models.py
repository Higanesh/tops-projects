from django.db import models

# Create your models here.
class Myuser(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=20)
