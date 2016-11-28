# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/migrations/0001_initial.py

from __future__ import unicode_literals

from django.db import (
    models,
    migrations,
)
from django.conf import settings

from simple_help.utils import modeltranslation


MODELTRANSLATION_FIELDS = [("title_{language}".format(**{"language": language, }), models.CharField(max_length=255, null=True, verbose_name="help title", db_index=True)) for language in list(dict(settings.LANGUAGES).keys())] + [("text_{language}".format(**{"language": language, }), models.TextField(null=True, verbose_name="help text")) for language in list(dict(settings.LANGUAGES).keys())] if modeltranslation() else []


class Migration(migrations.Migration):

    dependencies = []
    operations = [
        migrations.CreateModel(
            name="PageHelp",
            fields=[
                ("id", models.AutoField(verbose_name="ID", serialize=False, auto_created=True, primary_key=True)),
                ("page", models.IntegerField(default=0, unique=True, verbose_name="page", db_index=True)),
                ("title", models.CharField(max_length=255, verbose_name="help title", db_index=True)),
                ("text", models.TextField(verbose_name="help text")),
            ] + MODELTRANSLATION_FIELDS,
            options={
                "verbose_name": "page help",
                "verbose_name_plural": "page help",
            },
            bases=(models.Model, ),
        ),
    ]
