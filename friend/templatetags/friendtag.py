#_*_coding:utf-8_*_
from django import template
from friend.models import Friend

register = template.Library()   #чтобы объяснить, что это шаблонный тег

def upper(string):
    return string.upper()

def count_confirm(user):
    count = Friend.objects.claims(user).count()
    return count

#def check_friend(user):
#    check = Friend.objects.get_friend_status(user)
#    return check

register.simple_tag(upper, name='up')     # регистрируем шаблонный тег
#register.simple_tag(check_friend, name='check_friend')

register.simple_tag(count_confirm, name='count_confirm')