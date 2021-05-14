#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="plug-email-chase",
    version='1.0.1',
    description="Plug - Email Chase Pipeline",
    author="Lorenzo Coacci",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
    ],
    keywords=['data pipeline', 'etl', 'data engineering'],
    license=license,
    url="https://github.com/lollococce/plug-email-chase",
    include_package_data=True,
    install_requires=[
        'pytz==2018.4',
        'jsonschema==2.6.0',
        'simplejson==3.11.1',
        'python-dateutil>=2.6.0',
        'backoff==1.8.0',
        'ciso8601',
    ],
    extras_require={
        'dev': [
            'pylint',
            'ipython',
            'ipdb',
            'nose'
        ]
    },
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={
        'singer': [
            'logging.conf'
        ]
    }
)
