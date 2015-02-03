.. django-simple-help
.. README.rst

A django-simple-help documentation
==================================

    *django-simple-help is a django reusable application providing django project page help*

.. contents::

Installation
------------
* Obtain your copy of source code from git repository: ``git clone https://bitbucket.org/DCOD/django-simple-help.git``.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-simple-help``.

Configuration
-------------
Add ``'simple_help'``, ``'redactor'``, ``'dcl'`` and ``'modeltranslation'`` to ``settings.INSTALLED_APPS``.

    INSTALLED_APPS = (
        ...,

        'redactor',
        'modeltranslation',
        'dcl',
        'simple_help',

        ...,

    )

And additionally configure these apps as you want.

This library require additional static libraries, that must be placed in project static directory in ``lib`` subdirectory:

 - jQuery==1.11.2  # http://jquery.com/
 - bootstrap==3.3.2  # http://getbootstrap.com/

Add to project settings something like:

    INDEX_PAGE_HELP, CONTACT_PAGE_HELP = range(1, 3)
    SIMPLE_HELP_CHOICES = [
        [INDEX_PAGE_HELP, u'Index page help'],
        [CONTACT_PAGE_HELP, u'Contact page help'],
    ]

If you use bootstrap in you project include ``help_button.html`` template to base template.
Add to you page view context variable named ``PAGE_HELP`` with value of help you want to show.
Load ``help_tags`` into page template and call ``page_help`` tag.

Licensing
---------
django-simple-help is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://bitbucket.org/DCOD/django-simple-help

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>
