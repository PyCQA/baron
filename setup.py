#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='baron',
      version='0.1.1',
      description='Full Syntax Tree for python to make writing refactoring code a realist task',
      author='Laurent Peuch',
      long_description=open("README.md", "r").read(),
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/baron',
      install_requires=['rply'],
      packages=['baron'],
      license='lgplv3+',
      scripts=[],
      keywords='ast fst refactoring',
      )
