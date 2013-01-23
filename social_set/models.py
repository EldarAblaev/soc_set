#_*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import User as sUser
from datetime import date

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
)

class User(models.Model):
    user = models.ForeignKey(sUser, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    #f_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday = models.DateField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __unicode__(self):      #вывидит имя пользователя в админ панели
        return self.user.username

    @models.permalink
    def get_absolute_url(self):     #получение ссылки  на объект
        return ('other_profile', [self.user_id])
    #get_absolute_url = models.permalink(get_absolute_url)

def create_profile(sender, instance,created, **kwargs):
    if created:
        profile = User()
        profile.user = instance
        profile.birthday = date.today()
        profile.save()

models.signals.post_save.connect(create_profile, sender=sUser)  # создать профайл при создании системного юзера

'''
class Friend(models.Model):
    from_user_id = models.IntegerField(max_length=11)
    to_user_id = models.IntegerField(max_length=11)
    status = models.CharField(max_length=6)
'''
'''
class Message(models.Model):
    from_user_id = models.IntegerField(max_length=10)
    to_user_id = models.IntegerField(max_length=11)
    status_from = models.CharField(max_length=6, default='new')
    status_to = models.CharField(max_length=6, default='new')
    text = models.TextField()
    created_at = models.DateField(auto_now=True)

class Group(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    user_id = models.IntegerField(max_length=11)
    type = models.CharField(max_length=7)
    created_at = models.DateField(auto_now=True)
'''

class GroupMember(models.Model):
    group_id = models.IntegerField(max_length=11)
    user_id = models.IntegerField(max_length=11)
    role_in_group = models.CharField(max_length=20)

class GroupItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    group_id = models.IntegerField(max_length=11)
    created_at = models.DateField(auto_now=True)

class GroupItemComment(models.Model):
    group_item_id = models.IntegerField(max_length=11)
    text = models.TextField()
    parent_id = models.IntegerField(max_length=11)
    user_id = models.IntegerField(max_length=11)
    created_at = models.DateField(auto_now=True)

class UserFriendGroup(models.Model):
    user_id = models.IntegerField(max_length=11)
    friend_group_id = models.IntegerField(max_length=11)
    friend_id = models.IntegerField(max_length=11)

class FriendGroup(models.Model):
    name = models.CharField(max_length=255)

class Attachment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    media_id = models.IntegerField(max_length=11)
    resource_id = models.IntegerField(max_length=11)

class Media(models.Model):
    type = models.CharField(max_length=10)
    link = models.CharField(max_length=255)

class New(models.Model):
    who = models.CharField(max_length=100)
    what = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    pattern_id = models.IntegerField(max_length=2)
    created_at = models.DateField(auto_now=True)

class Pattern(models.Model):
    pattern = models.CharField(max_length=255)