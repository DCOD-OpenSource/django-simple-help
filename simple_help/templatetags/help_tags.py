# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/templatetags/help_tags.py

from django import template

from annoying.functions import get_object_or_None

from simple_help.models import PageHelp
from simple_help.settings import PAGE_HELP_MODAL_ADDITIONAL_CLASSES

__all__ = ['page_help', 'page_help_modal_additional_classes', ]


register = template.Library()


@register.assignment_tag(takes_context=True)
def page_help(context):
    """
    Page help.
    """

    if context.get('PAGE_HELP', None):
        return get_object_or_None(PageHelp, page=context['PAGE_HELP'])
    else:

        return None


@register.assignment_tag(takes_context=True)
def page_help_modal_additional_classes(context):
    """
    Page help modal additional classes.
    """

    return PAGE_HELP_MODAL_ADDITIONAL_CLASSES
