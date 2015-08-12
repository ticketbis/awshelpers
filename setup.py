#!/usr/bin/env python

from setuptools import setup, find_packages

requires_file = open('requirements.txt','r')
# print requires_file.readlines()

setup(name='AwsHelpers',
    version='0.1',
    description='AWS Helpers - to accelerate hard jobs with AWS',
    author='Eloy Garcia-Borreguero',
    author_email='eloygbm@gmail.com',
    platforms='any',
    license="Apache v2",
    scripts=['bin/awshelpers'],
    install_requires=requires_file.readlines(),
    packages=find_packages(),
    zip_safe=False
    )

# ,
    # py_modules=['awshelpers/lib/awsroute53helper','awshelpers/lib/__init__','awshelpers/main','awshelpers/local_settings','awshelpers/__init__']