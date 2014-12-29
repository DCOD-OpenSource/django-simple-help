# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageHelp'
        db.create_table(u'help_pagehelp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.IntegerField')(default=0, unique=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('title_ru', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('title_uk', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, null=True, blank=True)),
            ('text', self.gf('tinymce.models.HTMLField')()),
            ('text_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_ru', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('text_uk', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal('help', ['PageHelp'])


    def backwards(self, orm):
        # Deleting model 'PageHelp'
        db.delete_table(u'help_pagehelp')


    models = {
        'help.pagehelp': {
            'Meta': {'object_name': 'PageHelp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True', 'db_index': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {}),
            'text_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'text_uk': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['help']