#!/usr/bin/env python
import os
from setuptools import setup

setup(name='finsentiment',
      version='0.1',
      description='Python sentiment analysis utilities',
      author='Marc CHAN',
      author_email='marc.w.chan@gmail.com',
      packages=['finsentiment'],
      package_dir={'finsentiment': 'finsentiment'},
      install_requires=['numpy', 'pandas'],
      include_package_data=True,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",])
