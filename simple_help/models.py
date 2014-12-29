# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/models.py

from django.db import models
from django.utils.translation import ugettext_lazy as _

from simple_help.settings import PAGE_HELP_CHOICES

__all__ = ['PageHelp', ]


class PageHelp(models.Model):

    page = models.IntegerField(choices=PAGE_HELP_CHOICES, default=0, verbose_name=_(u'page'), db_index=True, unique=True)
    title = models.CharField(max_length=255, verbose_name=_(u'help title'), db_index=True)
    text = models.TextField(verbose_name=_(u'help text'))

    def __unicode__(self):

        return self.title

    class Meta:

        app_label = 'help'
        verbose_name = _(u'page help')
        verbose_name_plural = _(u'page help')
