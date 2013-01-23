from django import template
from groups.models import Group

register = template.Library()

def is_my_group(group_id, user_id):
    count = Group.objects.get(pk=group_id).users.filter(id=user_id).count()
    return {'count': count, 'group_id': group_id}

#register.simple_tag(is_my_group, name="check_group")
register.inclusion_tag("groups/check_group.html")(is_my_group)