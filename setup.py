#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import os
import sys
import boto3

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup


packages = [
    'boto3',
    'boto3.core',
    'boto3.core.resources',
    'boto3.ec2',
    'boto3.elastictranscoder',
    'boto3.glacier',
    'boto3.iam',
    'boto3.s3',
    'boto3.ses',
    'boto3.sns',
    'boto3.sqs',
    'boto3.utils',
]

requires = [
    'botocore==0.16.0',
    'six>=1.4.0',
    'jmespath>=0.0.2',
    'python-dateutil>=2.1',
]

setup(
    name='boto3',
    version=boto3.get_version(),
    description='Low-level, data-driven core of boto 3.',
    long_description=open('README.rst').read(),
    author='Amazon Web Services',
    author_email='garnaat@amazon.com',
    url='https://github.com/boto/boto3',
    scripts=[],
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    license=open("LICENSE").read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
