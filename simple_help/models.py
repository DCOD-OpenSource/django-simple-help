# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/models.py

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from simple_help.settings import PAGE_HELP_CHOICES


__all__ = [
    "PageHelp",
]


class PageHelp(models.Model):
    """
    Help model.
    """

    HELP_CHOICES = PAGE_HELP_CHOICES

    page = models.IntegerField(choices=HELP_CHOICES, default=0, verbose_name=_("page"), db_index=True, unique=True)
    title = models.CharField(max_length=255, verbose_name=_("help title"), db_index=True)
    text = models.TextField(verbose_name=_("help text"))

    def __str__(self):

        return self.title

    def __unicode__(self):

        return self.__str__()

    class Meta:

        app_label = "simple_help"
        verbose_name = _("page help")
        verbose_name_plural = _("page help")
