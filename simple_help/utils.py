# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/utils.py

from __future__ import unicode_literals

from django.conf import settings


__all__ = [
    "modeltranslation",
]


def modeltranslation():
    """
    Return modeltranslation usage.
    Returns:
        bool: modeltranslation usage.
    """

    return all([len(getattr(settings, "LANGUAGES", [])), "modeltranslation" in getattr(settings, "INSTALLED_APPS", [])], )
