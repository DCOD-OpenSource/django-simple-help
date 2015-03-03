# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PageHelp.title_zh_cn'
        db.add_column(u'simple_help_pagehelp', 'title_zh_cn',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PageHelp.text_zh_cn'
        db.add_column(u'simple_help_pagehelp', 'text_zh_cn',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PageHelp.title_zh_cn'
        db.delete_column(u'simple_help_pagehelp', 'title_zh_cn')

        # Deleting field 'PageHelp.text_zh_cn'
        db.delete_column(u'simple_help_pagehelp', 'text_zh_cn')


    models = {
        'simple_help.pagehelp': {
            'Meta': {'object_name': 'PageHelp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_zh_cn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_zh_cn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['simple_help']
