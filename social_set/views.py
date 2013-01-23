from django.contrib.auth import views,authenticate
from django.contrib.auth.models import User as sUser
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
#from django.views.generic.create_update import create_object
from social_set.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from friend.models import Friend
from messages.models import Message

def only_anonymous(function=None, redirect_to=None):
    from django.shortcuts import redirect
    def wrap(request, **kwargs):
        if not request.user.is_anonymous():
            return redirect(redirect_to)
        else:
            return function(request, **kwargs)

    return wrap



'''
def enter(request):

    if request.user.is_anonymous:
        print 'anonym'
    else:
        print 'not anonym'

    return redirect('profile/settings')
'''
def login(request):

    if request.POST:
        print 'post'
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user and user.is_active:
            views.login(request=request)
            #print request.user.id
            #return render(request, 'profile.html', {'user':user})
            return redirect('/profile')
            #return render_to_response('main.html', {'users':'not login'})
            #return redirect('profile/'+request.user.id)
        else:
            return render(request, 'auth.html')

    if request.method == 'GET':
        return redirect('/')
        #return render(request, 'auth.html')



def homepage(request):
    return render(request, 'auth.html')
homepage = only_anonymous(homepage, '/profile')

'''
    if request.method == 'GET':
    #else:
        print request.user
        if request.user.is_anonymous():
            print 'anonym'
            return render(request, 'auth.html')
        else:
            print 'not anonym'
            return render(request, 'profile.html', {'user':request.user})
            #return redirect('profile/'+request.user.id)

    #return redirect('profile/settings')
'''



def logout(request):
    views.logout(request=request)
    print 'logout'
    return redirect('/')

def register(request):

    if request.POST:
        user = sUser()
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password', ''))
        user.save()

        auth_user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if auth_user and auth_user.is_active:
            views.login(request, auth_user)
            print 'good'
            #return render(request, 'profile.html', {'user':auth_user})
            return redirect('profile/settings')
        else:
            print 'bad'
            return redirect('/')

    else:
    #if request.GET:
        return render(request, 'registration.html')
        #return redirect('/')
        #return create_object(request, {'model':sUser, 'post_save_redirect':'/', 'template_name':'forms/register.html'})
register=only_anonymous(register, '/')


class Form(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['user']

#@login_required
def profile(request, id=None):

    try:
        is_friend = False
        claims = 0
        if id is not None:
            user_cur = sUser.objects.get(pk=id)


            if id != request.user.id:
                is_friend = Friend.objects.is_friend(request.user, user_cur)
                if is_friend:
                    is_friend = is_friend[0]
        else:
            user_cur = request.user

        claims = Friend.objects.claims(user_cur).count()
        count_messages = Message.objects.count_new_mess(user_cur).count()
        print count_messages
        return render(request, 'profile.html', {'user_cur':user_cur, 'id':id, 'is_friend':is_friend, 'claims': claims})
#        else:
#            user_cur = request.user.get_profile()
#            #user_other = user
#        #return render(request, 'profile.html', {'user':user, 'user_cur':user_other})
#            return render(request, 'profile.html', {'user_cur':user_cur, 'id':user_cur.user.id})
        #return render(request, 'profile.html', {'user':request.user})
    except Exception, e:
        print e
        return redirect('/')



profile=login_required(profile, login_url='/login')

#@login_required
def edit_profile(request):
    form = Form(instance=request.user.get_profile())

    if request.POST:
        form = Form(request.POST, request.FILES, instance=request.user.get_profile())
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'forms/settings.html', {'form':form})
    else:
        return render(request, 'forms/settings.html', {'form':form})

edit_profile = login_required(edit_profile, login_url='/login')

#def all_users(request):
 #   return