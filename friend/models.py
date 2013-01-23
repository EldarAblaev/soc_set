#_*_coding:utf-8_*_
from django.db import models
#from social_set.models import User
from django.contrib.auth.models import User as sUser

STATUSES = (
    ('active', 'active'),
    ('follow', 'follow'),
)
class FriendManager(models.Manager):
    def get_friends(self, user):
        #return self.extra(where=['from_user_id = %d OR to_user_id = %d' % (user.id,user.id)])
        return self.extra(where=['from_user_id = %d AND status = "active"' % (user.id)])


    def is_friend(self, from_user, to_user):
        #return self.extra(where=['from_user_id = %d AND to_user_id = %d AND status = "act"' % (from_user.id, to_user.id)]).count()
        return self.extra(where=['from_user_id = %d AND to_user_id = %d' % (from_user.id, to_user.id)])
        #return self.extra(where=['to_user_id = %d AND status = "act"' % (to_user.id)])

    def claims(self, user_cur):
        return self.extra(where=['to_user_id = %d  AND status = "follow"' % (user_cur.id)])

    def is_confirm_friend(self, user_cur, friend):
        return self.extra(where=['from_user_id = %d AND to_user_id = %d AND status="follow"' % (friend.id, user_cur.id)]).count()


class Friend(models.Model):
    from_user = models.ForeignKey(sUser, related_name='+')
    to_user = models.ForeignKey(sUser, related_name='to_user_friends')
    status = models.CharField(max_length=100, choices=STATUSES)
    objects = FriendManager()

    def __unicode__(self):
        return '%s and %s are friends'%(self.from_user, self.to_user)

    @models.permalink
    def get_absolute_url(self):
        return ('other_profile', [self.to_user_id])

    #def is_friend(self):
        #print "is_friend"
        #return True

    #Friend.objects = FriendManager()


#f = Friend()
#f.objects.get_friend(user)