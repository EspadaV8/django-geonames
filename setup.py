#!/usr/bin/env python

from distutils.core import setup

setup(name='django-geonames',
      version='1.0',
      description='Fork of official GeoDjango geonames application refactored and adopted for Django 1.2.1',
      author='Justin Bronn',
      author_email='jbronn@geodjango.org',
      url='https://github.com/ramusus/django-geonames/',
      packages=['geonames', 'geonames.management', 'geonames.management.commands'],
      package_data={'geonames': ['sql']},
)

