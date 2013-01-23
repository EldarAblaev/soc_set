from django.db import models
from django.contrib.auth.models import User as sUser

TYPES = (
    ('public', 'public'),
    ('private', 'private'),
)

#class GroupManager(models.Manager):
#    def get_all_users(self):
#        return self.extra(where=['users'])

class Group(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    owner = models.ForeignKey(sUser, related_name='my_own_groups')
    users = models.ManyToManyField(sUser, related_name='my_groups')
    type = models.CharField(max_length=7, choices=TYPES)
    created_at = models.DateField(auto_now=True)
    #objects =GroupManager()

    def __unicode__(self):
        return self.name