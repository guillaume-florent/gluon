#!/usr/bin/env python
# coding: utf-8**

"""setuptools based setup module for gluon"""

from setuptools import setup
# To use a consistent encoding
import codecs
from os import path

import gluon

here = path.abspath(path.dirname(__file__))

# Get the long description from the README_SHORT file
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=gluon.__name__,
    version=gluon.__version__,
    description=gluon.__description__,
    long_description=long_description,
    url=gluon.__url__,
    download_url=gluon.__download_url__,
    author=gluon.__author__,
    author_email=gluon.__author_email__,
    license=gluon.__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='ui auto generation wx qt',
    packages=['gluon', 'gluon.ui'],
    install_requires=['atom'],  # requires atom and wxpython that should be
                                # installed with conda
    extras_require={
        'dev': [],
        'test': ['pytest', 'coverage'],
    },
    package_data={},
    data_files=[],
    entry_points={}
    )
