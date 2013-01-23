from django.db import models
from django.contrib.auth.models import User as sUser

class Photo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

#class Attachment(models.Model):
#    name = models.CharField(max_length=255)
#    description = models.TextField()
#    owner = models.ForeignKey(sUser, related_name="owner")
#    media_id = models.IntegerField(max_length=11)
#
#class Media(models.Model):
#    type = models.CharField(max_length=10)
#    link = models.CharField(max_length=255)
#    attach_id = models.ForeignKey(Attachment)