# -*- coding: utf-8 -*-
"""Fram basic bootstraping module."""

from setuptools import setup

__author__ = "Shawn Lee"
__email__ = "dashawn@gmail.com"
__license__ = "MIT"

major = 0
minor = 1
stamp = 3

short_description = "Fram basic bootstraping module."

setup(
    name="python-fram",
    version=".".join([str(x) for x in [major, minor, stamp]]),
    description=short_description,
    author="Shawn Lee",
    author_email="dashawn@gmail.com",
    url="https://github.com/dashawn888/fram",
    packages=["fram"],
    package_dir={"fram": "fram"},
    tests_require=["coverage", "mox", "nose2"],
    test_suite="fram_test",
    keywords=["cli", "framework", "argparse"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules"])
