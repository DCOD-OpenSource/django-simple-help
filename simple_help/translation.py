# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/translation/.py

from modeltranslation.translator import translator, TranslationOptions

from simple_help.models import PageHelp

__all__ = ['PageHelpTranslationOptions', ]


class PageHelpTranslationOptions(TranslationOptions):
    """
    PageHelp model translation options.
    """

    fields = ('title', 'text', )


# registering translation options
translator.register(PageHelp, PageHelpTranslationOptions)
