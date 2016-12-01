.. django-simple-help
.. README.rst

A django-simple-help documentation
==================================

    *django-simple-help is a django reusable application providing page help*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/DCOD-OpenSource/django-simple-help.git``. Or download the latest release from https://github.com/DCOD-OpenSource/django-simple-help/tags/.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-simple-help``.
* If you want to use simple help with `django-modeltranslation <https://github.com/deschler/django-modeltranslation/>`_ - install with additional requirements ``pip install django-simple-help[modeltranslation]``.

Configuration
-------------
Add ``"simple_help"`` and ``"redactor"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "redactor",
        "simple_help",
    )


If you want to use simple help with `django-modeltranslation <https://github.com/deschler/django-modeltranslation/>`_ - add ``"modeltranslation"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "modeltranslation",
    )


And additionally, configure these apps as you want.

Add to project settings something like:

.. code-block:: python

    INDEX_PAGE_HELP, CONTACT_PAGE_HELP = range(1, 3)
    SIMPLE_HELP_CHOICES = [
        [INDEX_PAGE_HELP, "Index page help"],
        [CONTACT_PAGE_HELP, "Contact page help"],
    ]


Usage
-----
Add to you page view context variable named ``PAGE_HELP`` with a value of help you want to show.
Load ``help_tags`` into page template and call ``page_help`` tag.
If you use `Bootstrap <https://getbootstrap.com/>`_ in you project include ``simple_help/includes/help_button.html`` and ``simple_help/includes/help_dialog.html`` templates to base template, else override default templates as you wish.

For example:

.. code-block:: django

    {% load help_tags %}

    {% page_help as page_help %}
    {% include "simple_help/includes/help_button.html" %}
    {% include "simple_help/includes/help_dialog.html" %}


Licensing
---------
django-simple-help uses the MIT license. Please check the MIT-LICENSE file for more details.


Contacts
--------
**Project Website**: https://github.com/DCOD-OpenSource/django-simple-help/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.
