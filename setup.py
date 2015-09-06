# coding: utf-8
__author__ = 'chedv13'

from distutils.core import setup
from setuptools import find_packages

with open('requirements/local.txt') as f:
    required = f.read().splitlines()

setup(name="taskbox",
      author="Dmitr Chekurov",
      author_email="chedv13@gmail.com",
      url="http://taskbox.com",
      version="0.1",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=required,
      )
