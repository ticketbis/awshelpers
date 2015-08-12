#!/usr/bin/env python
"""
    Setup info
"""
from setuptools import setup, find_packages

REQUIREMENTS_FILE = open('requirements.txt', 'r')

setup(name='AwsHelpers',
    version='0.1',
    description='AWS Helpers - to accelerate hard jobs with AWS',
    author='Eloy Garcia-Borreguero',
    author_email='eloygbm@gmail.com',
    platforms='any',
    license="Apache v2",
    scripts=['bin/awshelpers'],
    install_requires=REQUIREMENTS_FILE.readlines(),
    packages=find_packages(),
    zip_safe=False
    )
