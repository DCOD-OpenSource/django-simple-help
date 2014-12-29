# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/translation/.py

from modeltranslation.translator import TranslationOptions

__all__ = ['PageHelpTranslationOptions', ]


class PageHelpTranslationOptions(TranslationOptions):
    """
    PageHelp model translation options.
    """

    fields = ('title', 'text', )
