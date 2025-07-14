#!/usr/bin/env python3
"""Setup script for autarch"""

from setuptools import setup, find_packages

setup(
   name="autarch",
   use_scm_version=True,
   setup_requires=["setuptools_scm"],
   packages=find_packages(),
   scripts=["bin/autarch"],
)
