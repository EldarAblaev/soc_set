from django import template
from messages.models import Message

register = template.Library()

def mess_new_count(user):
    count = Message.objects.count_new_mess(user).count()
    return {'count': count}

register.inclusion_tag("messages/mess_new_count.html")(mess_new_count)