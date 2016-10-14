"""Fram basic bootstraping module."""

__author__ = "Shawn Lee"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from datetime import datetime

major = 0
minor = 1
stamp = 1

setup(
    name="python-fram",
    version=".".join([str(x) for x in [major, minor, stamp]]),
    description="Fram basic bootstraping module.",
    author="Shawn Lee",
    author_email="shawn@143t.com",
    packages=["fram"],
    package_dir={"fram": "fram"},
    options={ "bdist_rpm": {
            "requires": [
                "python-argparse"]}},
    tests_require=["coverage", "mox"],
    test_suite = "tests"
)
