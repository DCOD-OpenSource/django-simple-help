# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/admin.py

from __future__ import unicode_literals

from django.contrib import admin

try:  # add modeltranslation
    from modeltranslation.translator import translator
    from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin
except ImportError:
    pass

from simple_help.models import PageHelp
from simple_help.forms import PageHelpAdminForm
from simple_help.utils import modeltranslation
try:
    from simple_help.translation import PageHelpTranslationOptions
except ImportError:
    pass


__all__ = [
    "PageHelpAdmin",
]


class PageHelpAdmin(TabbedDjangoJqueryTranslationAdmin if modeltranslation() else admin.ModelAdmin):
    """
    Customize PageHelp model for admin area.
    """

    list_display = ["page", "title", ]
    search_fields = ["title", ]
    list_filter = ["page", ]

    form = PageHelpAdminForm


if modeltranslation():
    # registering translation options
    translator.register(PageHelp, PageHelpTranslationOptions)


# registering admin custom classes
admin.site.register(PageHelp, PageHelpAdmin)
