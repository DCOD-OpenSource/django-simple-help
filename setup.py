#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-simple-help
# setup.py

from setuptools import (
    setup,
    find_packages,
)


# metadata
VERSION = (0, 0, 0)
__version__ = ".".join(map(str, VERSION))
setup(
    name="django-simple-help",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "django-annoying==0.10.3",
        "django-wysiwyg-redactor==0.4.9.1",
    ],
    extras_require={
        "modeltranslation": ["django-modeltranslation==0.12", ],
    },
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Django reusable application providing django project page help",
    license="GPLv3 or later",
    url="https://github.com/DCOD-OpenSource/django-simple-help/",
    download_url="https://github.com/DCOD-OpenSource/django-simple-help/archive/{}.tar.gz".format(__version__),
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
