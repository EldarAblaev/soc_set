from groups.models import Group
from django.shortcuts import render, redirect
from django.core import urlresolvers
from django import forms

def allGroups(request):
    all_groups = Group.objects.all()
    return render(request, 'groups/all_groups.html', {'all_groups':all_groups})

def group(request, id=None):

    # Join group
    if request.GET:
        if request.GET['action'] == 'join':
            print request.GET
            group = Group.objects.get(pk=id)
            group.users.add(request.user)
            pass
        if request.GET['action'] == 'delete':
            print 'good'
            group = Group.objects.get(pk=id)
            group.users.remove(request.user)
            pass

    # Get group
    if id is not None:
        try:
            group = Group.objects.get(id=id)
            rnd_users = group.users.all()[0:6]
            return render(request, 'groups/group.html', {'group':group, 'rnd_users':rnd_users})
        except:
            pass

    return redirect(urlresolvers.reverse('allGroups'))

def groupUsers(request, id=None):

    if id is not None:
        try:
            group_users = Group.objects.get(id=id).users.all()
            return render(request, 'groups/group_users.html', { 'group_users':group_users })
        except Exception:
            pass

    return redirect(urlresolvers.reverse('allGroups'))

def createGroup(request):
    form = Form(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(urlresolvers.reverse('allGroups'))

    return render(request, 'groups/create_group.html', {'form': form})

class Form(forms.ModelForm):
    class Meta:
        model = Group