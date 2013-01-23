from django.contrib.auth.models import User

__author__ = 'secl'

def curent_user(request, id=None):

    if id:
        user = User.objects.get(pk=id)
    else:
        user= request.user
    return {'user_cur': user, 'TTT':1}