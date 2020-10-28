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
    description='Library for accessing EVE Online Swagger API\'s',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst',
        ),
    ).read(),
    author='Digium, Inc. , Yelp, Inc. and Gabriel Aguiar',
    author_email='opensource+aguiargab@gmail.com',
    url='https://github.com/Yelp/bravado',
    packages=find_packages(exclude=['tests/']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    package_data={
        'easy_esi': ['py.typed'],
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
        'fido': ['fido >= 4.2.1'],
        ':python_version<"3.5"': ['typing'],
        'integration-tests': [
            'bottle',
            'ephemeral_port_reserve',
            'pytest',
        ],
    },
    python_requires='!=3.0,!=3.1,!=3.2,!=3.3,!=3.4,!=3.5.0',
)
