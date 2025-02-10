from django.db import models

class MyUser(models.Model):
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)  
    lname = models.CharField(max_length=30)  

    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname}"  # String representation in admin
