# coding: utf-8
__author__ = 'chedv13'

from distutils.core import setup
from setuptools import find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements/base.txt', session=False)

#
# with open('requirements/local.txt') as f:
#     required = f.read().splitlines()
reqs = [str(ir.req) for ir in install_reqs]

setup(name="taskbox",
      author="Dmitr Chekurov",
      author_email="chedv13@gmail.com",
      url="http://taskbox.com",
      version="0.1",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=reqs,
      )
