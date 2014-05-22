#!/usr/bin/env python

from distutils.core import setup

setup(name='AwsHelpers',
    version='0.1',
    description='AWS Helpers - to accelerate hard jobs with AWS',
    author='Eloy Garcia-Borreguero',
    author_email='eloygbm@gmail.com',
    packages=find_packages(),
    platforms='any',
    scripts=['bin/awshelpers'],
    py_modules=['awshelpers/lib/awsroute53helper','awshelpers/lib/__init__','awshelpers/main','awshelpers/local_settings','awshelpers/__init__']
    )
