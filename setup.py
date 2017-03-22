# -*- coding: utf-8 -*-
"""Fram basic bootstraping module."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = "Shawn Lee"
__email__ = "dashawn@gmail.com"

major = 0
minor = 1
stamp = 3

setup(
    name="python-fram",
    version=".".join([str(x) for x in [major, minor, stamp]]),
    description="Fram basic bootstraping module.",
    author="Shawn Lee",
    author_email="dashawn@gmail.com",
    packages=["fram"],
    package_dir={"fram": "fram"},
    options={"bdist_rpm": {
            "requires": [
                "python-argparse"]}},
    tests_require=["coverage", "mox"],
    test_suite="tests"
)
