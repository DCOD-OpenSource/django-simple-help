# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/forms.py

from django import forms
from django.conf import settings

from annoying.decorators import autostrip
from dcl.widgets import RedactorEditorWithoutJQuery


__all__ = ['PageHelpAdminForm', ]


@autostrip
class PageHelpAdminForm(forms.ModelForm):
    """
    Custom form for page help admin.
    """

    class Meta:

        widgets = dict([(u'text_%s' % language.replace('-', '_'), RedactorEditorWithoutJQuery()) for language in dict(settings.LANGUAGES).keys()])
