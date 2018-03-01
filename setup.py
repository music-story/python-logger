#!/usr/bin/env python
# coding: utf-8

from setuptools import setup


setup(
    name='mslogger',
    version='1.0.0.dev1',
    description='Python Logger library for Music-Story dataflows',

    author='Music-Story',
    author_email='webmaster@music-story.com',

    package_dir={'musicstory.logger': 'lib'},
    packages=['musicstory.logger'],
    install_requires=[
        'python-dotenv>=0.7.1,<0.8',
    ],
)
