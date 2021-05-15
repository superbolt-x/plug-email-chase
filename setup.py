#!/usr/bin/env python

from setuptools import setup, find_packages


def long_description():
    with open("README.md", "r", encoding="utf-8") as rf:
        readme = rf.read()
    return readme


def license_file():
    with open("LICENSE", "r", encoding="utf-8") as rf:
        license_file = rf.read()
    return license_file


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
        "License :: OSI Approved :: Apache License 2.0",
        "Natural Language :: English",
    ],
    keywords=["data pipeline", "etl", "data engineering"],
    license=license_file(),
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
    extras_require={"dev": ["pylint", "black", "flake8", "pytest", "coverage"]},
    packages=find_packages(exclude=("tests", "tests.*", "docs", "docs.*")),
    package_data={"singer": ["logging.conf"]},
    zip_safe=False,
)
