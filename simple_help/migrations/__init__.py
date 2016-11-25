# -*- coding: utf-8 -*-

# django-simple-help
# simple_help/migrations/__init__.py

from django.core.exceptions import ImproperlyConfigured


SOUTH_ERROR_MESSAGE = """\n
For South support, customize the SOUTH_MIGRATION_MODULES setting like so:

    SOUTH_MIGRATION_MODULES = {
        'simple_help': 'simple_help.south_migrations',
    }
"""

# Ensure the user is not using Django 1.6 or below with South
try:
    from django.db import migrations
except ImportError:
    raise ImproperlyConfigured(SOUTH_ERROR_MESSAGE)
