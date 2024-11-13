from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)
    email =models.EmailField(blank=True, null=True)

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class Spam(models.Model):
    reporter= models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
