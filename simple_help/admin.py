# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/admin.py

from django.contrib import admin

from modeltranslation.translator import translator
from modeltranslation.admin import TranslationAdmin
from dcl.admin import ModelTranslationAdminMediaMixin

from simple_help.models import PageHelp
from simple_help.forms import PageHelpAdminForm
from simple_help.translation import PageHelpTranslationOptions

__all__ = ['PageHelpAdmin', ]


class PageHelpAdmin(TranslationAdmin, ModelTranslationAdminMediaMixin):
    """
    Customize PageHelp model for admin area.
    """

    list_display = ('page', 'title', )
    search_fields = ('title', )
    list_filter = ('page', )

    form = PageHelpAdminForm


# registering translation options
translator.register(PageHelp, PageHelpTranslationOptions)


# registering admin custom classes
admin.site.register(PageHelp, PageHelpAdmin)
