#!/usr/bin/env python

import re
from setuptools import setup, find_packages
import subprocess


def long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    return readme


def license():
    with open("LICENSE", "r", encoding="utf-8") as f:
        license = f.read()
    return license


setup(
    name="plug-email-chase",
    version="1.0.1",
    description="Plug - Email Chase Pipeline",
    author="Lorenzo Coacci",
    author_email="lorenzo@coacci.it",
    long_description_content_type="text/markdown",
    long_description=long_description(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
    keywords=["data pipeline", "etl", "data engineering"],
    license=license(),
    url="https://github.com/lollococce/plug-email-chase",
    include_package_data=True,
    install_requires=[
        "pytz==2018.4",
        "jsonschema==2.6.0",
        "simplejson==3.11.1",
        "python-dateutil>=2.6.0",
        "backoff==1.8.0",
        "ciso8601",
    ],
    extras_require={"dev": ["pylint", "ipython", "ipdb", "nose"]},
    packages=find_packages(exclude=("tests", "tests.*", "docs", "docs.*")),
    package_data={"singer": ["logging.conf"]},
    zip_safe=False,
)
