#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='swing',
      version='0.1',
      packages=find_packages(),
      package_data={'swing': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'swing': ['bin/*.pyc']},
      scripts=['swing/bin/manage.py'])
