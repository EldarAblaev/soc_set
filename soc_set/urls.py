from django.conf.urls import patterns, include, url
from soc_set.settings import STATIC_ROOT, MEDIA_ROOT, STAT_ROOT
from django.views.generic.list_detail import object_detail,object_list
from social_set.models import User
#from friend.models import Friend

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'social_set.views.homepage'),
    url(r'^login$', 'social_set.views.login', name='login'),
    url(r'^logout$', 'social_set.views.logout', name='logout'),
    url(r'^register$', 'social_set.views.register', name='register'),
    url(r'^profile/settings$', 'social_set.views.edit_profile', name='edit_profile'),
    #url(r'^register$', 'django.views.generic.simple.direct_to_template', {'template':'base.html'}),
    #url(r'^register$', 'django.views.generic.create_update.create_object', {'model':User, 'post_save_redirect':'/', 'template_name':'forms/register.html'}),
    #url(r'^$', 'django.views.generic.simple.direct_to_template', {'template':'main.html'}),
    # url(r'^soc_set/', include('soc_set.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^profile/(?P<object_id>(\d+))$', object_detail, {'template_name':'profile.html', 'queryset':User.objects.all()}),
    #url(r'^profile/(?P<object_id>(\d+))$', object_list, {'template_name':'profile.html', 'queryset':User.objects.all()}),
    url(r'^profile/$', 'social_set.views.profile', name='profile'),
    url(r'^profile/(?P<id>\d+)$', 'social_set.views.profile', name='other_profile'),
    url(r'^users/$', login_required(object_list), {'template_name':'users_list.html', 'queryset':User.objects.all()}, name='users'),

    url(r'^friends/$', 'friend.views.friends', name='friends'),
    url(r'^friends/(?P<id>\d+)$', 'friend.views.friends', name='friends_of_friend'),
    #url(r'^addfriend/(?P<id>\d+)$', 'friend.views.addToFriends'),
    #url(r'^addfriend/(?P<id>\d+)$', 'friend.views.addToFriends', name="addToFriends"),
    url(r'^addfriend/$', 'friend.views.addToFriends', name="addToFriends"),
    url(r'^delfriend/$', 'friend.views.delFriend', name='delFriend'),
    url(r'^messages/$', 'messages.views.allMessages', name="allMessages"),
    url(r'^message/(?P<id>\d+)$', 'messages.views.message', name="message"),
    url(r'^newmessage/(?P<id>\d+)$', 'messages.views.newMessage', name="newMessage"),
    url(r'^groups/$', 'groups.views.allGroups', name="allGroups"),
    url(r'^group/(?P<id>\d+)$', 'groups.views.group', name="group"),
    url(r'^group/create/$', 'groups.views.createGroup', name="createGroup"),
    #url(r'^group/$', 'groups.views.group', name="group"),
    url(r'^group/users/(?P<id>\d+)$', 'groups.views.groupUsers', name="groupUsers"),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':STATIC_ROOT}),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root':MEDIA_ROOT}),
    url(r'^stat/(?P<path>.*)', 'django.views.static.serve', {'document_root':STAT_ROOT}),
)