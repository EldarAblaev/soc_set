from django.db import models
from django.contrib.auth.models import User as sUser

class Fotoalbum(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Media(models.Model):
    type = models.CharField(max_length=10)
    link = models.CharField(max_length=255)