from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Notes(models.Model):
    userId = models.IntegerField(default=100)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.userId