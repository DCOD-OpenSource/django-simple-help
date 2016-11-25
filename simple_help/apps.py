# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/apps.py

from __future__ import unicode_literals

from django.apps import AppConfig


__all__ = [
    "Config",
]


class Config(AppConfig):

    name = "simple_help"
    verbose_name = "Simple help"
