# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/forms.py

from __future__ import unicode_literals

from django import forms
from django.conf import settings

from annoying.decorators import autostrip
from redactor.widgets import RedactorEditor

from simple_help.utils import modeltranslation


__all__ = [
    "PageHelpAdminForm",
]


@autostrip
class PageHelpAdminForm(forms.ModelForm):
    """
    Custom form for page help admin.
    """

    class Meta:

        if modeltranslation():
            widgets = dict([("text_{language}".format(**{"language": language.replace("-", "_"), }), RedactorEditor()) for language in list(dict(settings.LANGUAGES).keys())])
        else:
            widgets = {
                "text": RedactorEditor()
            }
