from django.db import models

# Create your models here.
class User(models.Model): #宣告user表
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=16)