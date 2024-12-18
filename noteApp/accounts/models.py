from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.IntegerField(default=1)
    userName = models.CharField(max_length=255)
    userEmail = models.CharField(max_length=255, unique=True)