from django.shortcuts import render
from friend.models import Friend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as sUser
from django.http import HttpResponse

@login_required
def friends(request, id=None):
    if id is not None:
        user_cur = sUser.objects.get(pk=id)
    else:
        user_cur = request.user
    friend_list = Friend.objects.get_friends(user_cur)
    claims = Friend.objects.claims(user_cur)
    f = True
    print user_cur

    return render(request, 'friends/list.html', {'friends':friend_list, 'user_cur': user_cur, 'claims':claims, 'is_friend': f})

def addToFriends(request):

    if request.is_ajax():
        id = request.GET.get('id')
        friend = sUser.objects.get(pk=id)

        is_confirm_friend = Friend.objects.is_confirm_friend(request.user, friend)

        if is_confirm_friend:
            Friend.objects.filter(from_user = friend, to_user = request.user).update(status='active')
            newRow = Friend(from_user = request.user, to_user = friend, status = 'active')
            newRow.save()
        else:
            newRow = Friend(from_user = request.user, to_user = friend, status = 'follow')
            newRow.save()

    return HttpResponse()

def delFriend(request):
    if request.is_ajax():
        id = request.GET.get('id')
        friend = sUser.objects.get(pk=id)

        Friend.objects.filter(from_user = friend, to_user = request.user).delete()
        Friend.objects.filter(from_user = request.user, to_user = friend).delete()

    return HttpResponse()