from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    img = models.ImageField(upload_to="img",null=True)

    def __str__(self):
        return self.name+' '+self.email
    

