from django.db import models

# Create your models here.
class Room(models.Model):
    code=models.CharField(max_length=8,default="",unique=True)
    
class Video(models.Model):
    code=models.CharField(max_length=20,default="",unique=True)
    
class Category(models.Model):
    code=models.CharField(max_length=20,default="",unique=True)
    