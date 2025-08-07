from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=30)

class UserRegistration(models.Model):
    fullname = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
   
class Adoptiondata(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address= models.TextField()
    type = models.CharField(max_length=50)
    reason = models.TextField()

    def __str__(self):
        return self.fullname
      
