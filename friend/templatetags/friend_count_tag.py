from django import template
from friend.models import Friend

register = template.Library()

def friend_count_confirm(user):
    count  = Friend.objects.claims(user).count()
    return {'count':count}

register.inclusion_tag("friends/friend_count_confirm.html")(friend_count_confirm)