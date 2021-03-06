#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013, Digium, Inc.
# Copyright (c) 2014-2016, Yelp, Inc.
import os

from setuptools import find_packages
from setuptools import setup

import easyesi

setup(
    name='easy-esi',
    version=easyesi.version,
    license='BSD 3-Clause License',
    description='Library for accessing EVE Online Swagger API',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst',
        ),
    ).read(),
    author='Digium, Inc. , Yelp, Inc. and Gabriel Aguiar',
    author_email='Gabriel Aguiar+aguiargab@gmail.com',
    url='https://github.com/12gabriel3/easy-esi',
    packages=find_packages(exclude=['tests/']),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    package_data={
        'easyesi': ['py.typed'],
    },
    install_requires=[
        "jsonref",
        "jsonschema[format]>=2.5.1",
        "pyyaml",
        "swagger-spec-validator>=2.0.1",
        "pytz",
        "msgpack>=0.5.2",
        'python-dateutil',
        'requests >= 2.17',
        'six',
        'simplejson',
        'monotonic',
        'typing_extensions',
    ],
    extras_require={
        'integration-tests': [
            'bottle',
            'ephemeral_port_reserve',
            'pytest',
        ],
    },
    python_requires='>=3.6',
)
