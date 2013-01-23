# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('social_set_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('birthday', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('social_set', ['User'])

        # Adding model 'Message'
        db.create_table('social_set_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('to_user_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('status_from', self.gf('django.db.models.fields.CharField')(default='new', max_length=6)),
            ('status_to', self.gf('django.db.models.fields.CharField')(default='new', max_length=6)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social_set', ['Message'])

        # Adding model 'Group'
        db.create_table('social_set_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social_set', ['Group'])

        # Adding model 'GroupMember'
        db.create_table('social_set_groupmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('role_in_group', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('social_set', ['GroupMember'])

        # Adding model 'GroupItem'
        db.create_table('social_set_groupitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('group_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social_set', ['GroupItem'])

        # Adding model 'GroupItemComment'
        db.create_table('social_set_groupitemcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_item_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social_set', ['GroupItemComment'])

        # Adding model 'UserFriendGroup'
        db.create_table('social_set_userfriendgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('friend_group_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('friend_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
        ))
        db.send_create_signal('social_set', ['UserFriendGroup'])

        # Adding model 'FriendGroup'
        db.create_table('social_set_friendgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('social_set', ['FriendGroup'])

        # Adding model 'Attachment'
        db.create_table('social_set_attachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('media_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
            ('resource_id', self.gf('django.db.models.fields.IntegerField')(max_length=11)),
        ))
        db.send_create_signal('social_set', ['Attachment'])

        # Adding model 'Media'
        db.create_table('social_set_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('social_set', ['Media'])

        # Adding model 'New'
        db.create_table('social_set_new', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('who', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('what', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pattern_id', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('social_set', ['New'])

        # Adding model 'Pattern'
        db.create_table('social_set_pattern', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pattern', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('social_set', ['Pattern'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('social_set_user')

        # Deleting model 'Message'
        db.delete_table('social_set_message')

        # Deleting model 'Group'
        db.delete_table('social_set_group')

        # Deleting model 'GroupMember'
        db.delete_table('social_set_groupmember')

        # Deleting model 'GroupItem'
        db.delete_table('social_set_groupitem')

        # Deleting model 'GroupItemComment'
        db.delete_table('social_set_groupitemcomment')

        # Deleting model 'UserFriendGroup'
        db.delete_table('social_set_userfriendgroup')

        # Deleting model 'FriendGroup'
        db.delete_table('social_set_friendgroup')

        # Deleting model 'Attachment'
        db.delete_table('social_set_attachment')

        # Deleting model 'Media'
        db.delete_table('social_set_media')

        # Deleting model 'New'
        db.delete_table('social_set_new')

        # Deleting model 'Pattern'
        db.delete_table('social_set_pattern')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'social_set.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'resource_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        },
        'social_set.friendgroup': {
            'Meta': {'object_name': 'FriendGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'social_set.group': {
            'Meta': {'object_name': 'Group'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        },
        'social_set.groupitem': {
            'Meta': {'object_name': 'GroupItem'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'social_set.groupitemcomment': {
            'Meta': {'object_name': 'GroupItemComment'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group_item_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        },
        'social_set.groupmember': {
            'Meta': {'object_name': 'GroupMember'},
            'group_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role_in_group': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        },
        'social_set.media': {
            'Meta': {'object_name': 'Media'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'social_set.message': {
            'Meta': {'object_name': 'Message'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'from_user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_from': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '6'}),
            'status_to': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '6'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'to_user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        },
        'social_set.new': {
            'Meta': {'object_name': 'New'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern_id': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'what': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'social_set.pattern': {
            'Meta': {'object_name': 'Pattern'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'social_set.user': {
            'Meta': {'object_name': 'User'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'social_set.userfriendgroup': {
            'Meta': {'object_name': 'UserFriendGroup'},
            'friend_group_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'friend_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'max_length': '11'})
        }
    }

    complete_apps = ['social_set']