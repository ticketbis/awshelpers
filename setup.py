#!/usr/bin/env python
"""
    Setup info
"""
from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

REQUIREMENTS_FILE = open('requirements.txt', 'r')

setup(name='awshelpers',
    version='0.1',
    description='AWS Helpers - to accelerate hard jobs with AWS Route53',
    long_description=readme(),
    url='http://github.com/ticketbis/awshelpers',
    author='Eloy Garcia-Borreguero',
    author_email='eloygbm@gmail.com',
    platforms='any',
    license="Apache v2",
    entry_points={
        'console_scripts': ['awshelpers=awshelpers.main:main'],
    },
    install_requires=REQUIREMENTS_FILE.readlines(),
    packages=find_packages(),
    keywords=['Route53'],
    zip_safe=False
    )
