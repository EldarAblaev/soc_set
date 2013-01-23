from django.db import models
from django.contrib.auth.models import User as sUser

STATUSES = (
    ('new', 'new'),
    ('read', 'read'),
    ('delete', 'delete'),
)

class MessageManager(models.Manager):
    def get_all_messages(self, user):
        return self.extra(where=['to_user_id = %d' % (user.id)])

    def count_new_mess(self, user):
        return self.extra(where=['to_user_id = %d AND status_to = "new"' % (user.id)])

class Message(models.Model):
    from_user = models.ForeignKey(sUser, related_name='+')
    to_user = models.ForeignKey(sUser, related_name='to_user_messages')
    status_from = models.CharField(max_length=6, choices=STATUSES)
    status_to = models.CharField(max_length=6, choices=STATUSES)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
    objects = MessageManager()

    def __unicode__(self):
        return "Message from %s to %s" % (self.from_user, self.to_user)