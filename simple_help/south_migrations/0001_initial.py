# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/south_migrations/0001_initial.py

from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration

from simple_help.utils import modeltranslation


def modeltranslation_fields(self):
    """
    Helper function for generating modeltranslation multi language fields.
    Args:
        self: (south.v2.SchemaMigration): Migrations instance.
    Returns:
        tuple: tuple with modeltranslation fields.
    """

    if modeltranslation():
        title = tuple([("title_{language}".format(**{"language": language, }), self.gf("django.db.models.fields.CharField")(db_index=True, max_length=255, null=True, blank=True)) for language in list(dict(settings.LANGUAGES).keys())])
        text = tuple([("text_{language}".format(**{"language": language, }), self.gf("django.db.models.fields.TextField")(null=True, blank=True)) for language in list(dict(settings.LANGUAGES).keys())])

        return title + text
    else:

        return tuple()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model "PageHelp"
        db.create_table("simple_help_pagehelp", (
                ("id", self.gf("django.db.models.fields.AutoField")(primary_key=True)),
                ("page", self.gf("django.db.models.fields.IntegerField")(default=0, unique=True, db_index=True)),
                ("title", self.gf("django.db.models.fields.CharField")(max_length=255, db_index=True)),
                ("text", self.gf("django.db.models.fields.TextField")()),
            ) + modeltranslation_fields(self)
        )

        db.send_create_signal("simple_help", ["PageHelp"])

    def backwards(self, orm):
        # Deleting model "PageHelp"
        db.delete_table(u"simple_help_pagehelp")

    models = {
        "simple_help.pagehelp": {
            "Meta": {"object_name": "PageHelp"},
            "id": ("django.db.models.fields.AutoField", [], {"primary_key": "True"}),
            "page": ("django.db.models.fields.IntegerField", [], {"default": "0", "unique": "True", "db_index": "True"}),
            "text": ("django.db.models.fields.TextField", [], {}),
            "title": ("django.db.models.fields.CharField", [], {"max_length": "255", "db_index": "True"}),
        }
    }

    if modeltranslation():
        for language in list(dict(settings.LANGUAGES).keys()):
            # add modeltranslation fields
            models["simple_help.pagehelp"].update({"title_{language}".format(**{"language": language, }): ("django.db.models.fields.TextField", [], {"null": "True", "blank": "True"})})
            models["simple_help.pagehelp"].update({"text_{language}".format(**{"language": language, }): ("django.db.models.fields.TextField", [], {"null": "True", "blank": "True"})})

    complete_apps = ["simple_help"]
