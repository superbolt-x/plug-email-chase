#!/usr/bin/env python
"""
setup
-----
Set up Py Package

Date: 2021-05-14

Author: Lorenzo Coacci
"""
from setuptools import setup, find_packages


def load_long_description():
    """Parse long description file"""
    with open("README.md", "r", encoding="utf-8") as f_readme:
        readme = f_readme.read()
    return readme


def load_license():
    """Parse license file"""
    with open("LICENSE", "r", encoding="utf-8") as f_license:
        license_file = f_license.read()
    return license_file


setup(
    name="plug-email-chase",
    version="1.0.1",
    description="Plug - Email Chase Pipeline",
    author="Lorenzo Coacci",
    author_email="lorenzo@coacci.it",
    long_description_content_type="text/markdown",
    long_description=load_long_description(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache License 2.0",
        "Natural Language :: English",
    ],
    keywords=["data pipeline", "etl", "data engineering"],
    license=load_license(),
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
    extras_require={"test": ["pylint", "black", "flake8", "pytest", "coverage"]},
    packages=find_packages(exclude=("tests", "tests.*", "docs", "docs.*")),
    package_data={"plug_email_chase": ["logging.conf"]},
    zip_safe=False,
)
