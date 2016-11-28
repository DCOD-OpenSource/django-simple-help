# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/translation.py

from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions


__all__ = [
    "PageHelpTranslationOptions",
]


class PageHelpTranslationOptions(TranslationOptions):
    """
    PageHelp modeltranslation options.
    """

    fields = ["title", "text", ]
