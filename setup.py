#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-simple-help
# setup.py

from setuptools import setup, find_packages

# metadata
VERSION = (0, 2, 1)
__version__ = '.'.join(map(str, VERSION))

setup(
    name="django-simple-help",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'django-modeltranslation==0.8',
        'django-wysiwyg-redactor==0.4.2.1',
    ],
    dependency_links=[
        "git+git@bitbucket.org:DCOD/dcod-common-lib.git#egg=dcl",
    ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Django reusable application providing django project page help",
    license="GPLv3 or later",
    url="https://github.com/vint21h/django-simple-help",
    download_url="https://github.com/vint21h/django-simple-help/archive/%s.tar.gz" % __version__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ]
)
