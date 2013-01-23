from messages.models import Message
from django.contrib.auth.models import User as sUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from friend.models import Friend

@login_required
def allMessages(request):
    allMessages = Message.objects.get_all_messages(request.user)
    return render(request, 'messages/all_messages.html', {'allMessages': allMessages, 'user_cur': request.user})

def message(request, id=None):

    '''
    if request.POST:
        to_user = Message.object.get(pk=id).from_user
        Message(from_user = request.user, to_user = to_user, text = request.POST.get('message_text')).save()
        return redirect('/messages')
    '''
    try:
        mess = Message.objects.filter(id=id)
        mess.update(status_to='read')
        mess = mess[0]
        from_user_id =  mess.from_user.id

        if mess is not None:
            return render(request, 'messages/message.html', {'message': mess, 'user_id': from_user_id, 'user_cur': request.user})

    except Exception, e:
        print e
        return redirect('/messages')

def newMessage(request, id=None):

    to_user = sUser.objects.get(pk=id)
    print to_user

    is_friend = False
    if id is not None:

        if id != request.user.id:
            is_friend = Friend.objects.is_friend(request.user, to_user)
            if is_friend:
                is_friend = is_friend[0]

    if request.POST:
        print 'post'
        print request.user
        print to_user
        Message(from_user = request.user, to_user = to_user, text = request.POST.get('message_text'), status_from = 'read', status_to = 'new').save();
        return redirect('/profile/' + id)

    return render(request, 'messages/new_message.html', {'message':'', 'user_id':id, 'user_cur': to_user, 'is_friend': is_friend, 'id': id})