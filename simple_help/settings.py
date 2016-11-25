# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/constants.py

from __future__ import unicode_literals

from django.conf import settings


__all__ = [
    "PAGE_HELP_CHOICES",
]


PAGE_HELP_CHOICES = getattr(settings, "SIMPLE_HELP_CHOICES", [])
