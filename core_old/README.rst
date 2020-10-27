.. image:: https://travis-ci.com/12gabriel3/easy-esi-core.svg?branch=renaming
    :target: https://travis-ci.com/12gabriel3/easy-esi-core

.. image:: https://coveralls.io/repos/github/12gabriel3/easy-esi-core/badge.svg
   :target: https://coveralls.io/github/12gabriel3/easy-esi-core

easy-esi-core
============

About
-----

easy-esi-core is a Python library that adds client-side and server-side support
for the `OpenAPI Specification v2.0 <https://github.com/OAI/OpenAPI-Specification>`__.

Features
--------
* OpenAPI Specification schema validation
* Marshaling, transformation, and validation of requests and responses
* Models as Python classes or dicts
* Custom formats for type conversion

Documentation
-------------

Documentation is available at `readthedocs.org <http://easy-esi-core.readthedocs.org>`__


Installation
------------

::

    $ pip install easy-esi-core


Related Projects
----------------
* `bravado <https://github.com/Yelp/bravado>`__
* `pyramid-swagger <https://github.com/striglia/pyramid_swagger>`__
* `swagger-spec-validator <https://github.com/Yelp/swagger_spec_validator>`__

Development
===========

| Code is documented using `Sphinx <http://sphinx-doc.org/>`__.
| `virtualenv <http://virtualenv.readthedocs.org/en/latest/virtualenv.html>`__ is recommended to keep dependencies and libraries isolated.
| `tox <https://tox.readthedocs.org/en/latest/>`__ is used for standardized testing.

Setup
-----

::

    # Run tests
    tox

    # Install git pre-commit hooks
    .tox/py27/bin/pre-commit install


Contributing
------------

1. Fork it ( http://github.com/12gabriel3/easy-esi-core/fork )
2. Create your feature branch (``git checkout -b my-new-feature``)
3. Add your modifications
4. Add short summary of your modifications on ``CHANGELOG.rst``
5. Commit your changes (``git commit -m "Add some feature"``)
6. Push to the branch (``git push origin my-new-feature``)
7. Create new Pull Request

License
-------

| Copyright (c) 2013, Digium, Inc. All rights reserved.
| Copyright (c) 2014-2015, Yelp, Inc. All rights reserved.

Bravado is licensed with a `BSD 3-Clause
License <http://opensource.org/licenses/BSD-3-Clause>`__.
