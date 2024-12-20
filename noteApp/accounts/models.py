from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    userId = models.IntegerField(default=100)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255,default='')

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
    ]
    def __str__(self):
        return self.userId