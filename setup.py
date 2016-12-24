#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-simple-help
# setup.py

from setuptools import (
    setup,
    find_packages,
)


# metadata
VERSION = (0, 6, 0)
__version__ = ".".join(map(str, VERSION))
setup(
    name="django-simple-help",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "Django",
        "django-annoying==0.10.3",
        "django-wysiwyg-redactor==0.4.9.1",
    ],
    extras_require={
        "modeltranslation": [
            "django-modeltranslation==0.12",
        ],
    },
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Django reusable application providing page help",
    license="MIT",
    url="https://github.com/DCOD-OpenSource/django-simple-help/",
    download_url="https://github.com/DCOD-OpenSource/django-simple-help/archive/{version}.tar.gz".format(**{"version": __version__, }),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
    ]
)
