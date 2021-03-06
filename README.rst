.. image:: https://travis-ci.com/12gabriel3/easy-esi.svg?branch=master
    :target: https://travis-ci.com/12gabriel3/easy-esi

.. image:: https://coveralls.io/repos/github/12gabriel3/easy-esi/badge.svg?branch=master
    :target: https://coveralls.io/github/12gabriel3/easy-esi?branch=master

EasyEsi
==========

About
-----

Easy ESIis a Yelp maintained fork of `digium/swagger-py <https://github.com/digium/swagger-py/>`__
for use with `OpenAPI Specification version 2.0 <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md>`__ (previously
known as Swagger).

From the OpenAPI Specification project:

    The goal of The OpenAPI Specification is to define a standard,
    language-agnostic interface to REST APIs which allows both humans and
    computers to discover and understand the capabilities of the service
    without access to source code, documentation, or through network traffic
    inspection.

Client libraries can automatically be generated from the OpenAPI specification,
however Easy ESI aims to be a complete replacement for code generation
(`swagger-codegen <https://github.com/wordnik/swagger-codegen>`__).

Example Usage
-------------

.. code-block:: Python

    from easy_esi.client import SwaggerClient
    client = SwaggerClient.from_url('http://petstore.swagger.io/v2/swagger.json')
    pet = client.pet.getPetById(petId=1).response().result

Example with Basic Authentication
---------------------------------

.. code-block:: python

    from easy_esi.requests_client import RequestsClient
    from easy_esi.client import SwaggerClient

    http_client = RequestsClient()
    http_client.set_basic_auth(
        'api.yourhost.com',
        'username', 'password'
    )
    client = SwaggerClient.from_url(
        'http://petstore.swagger.io/v2/swagger.json',
        http_client=http_client,
    )
    pet = client.pet.getPetById(petId=1).response().result

Example with Header Authentication
----------------------------------

.. code-block:: python

    from easy_esi.requests_client import RequestsClient
    from easy_esi.client import SwaggerClient

    http_client = RequestsClient()
    http_client.set_api_key(
        'api.yourhost.com', 'token',
        param_name='api-key', param_in='header'
    )
    client = SwaggerClient.from_url(
        'http://petstore.swagger.io/v2/swagger.json',
        http_client=http_client,
    )
    pet = client.pet.getPetById(petId=1).response().result

Example with Fido Client (Async Http Client)
--------------------------------------------

.. code-block:: python

    # Install bravado with fido extra (``pip install bravado[fido]``)
    from easy_esi.fido_client import FidoClient
    from easy_esi.client import SwaggerClient

    http_client = FidoClient()
    client = SwaggerClient.from_url(
        'http://petstore.swagger.io/v2/swagger.json',
        http_client=http_client,
    )
    pet = client.pet.getPetById(petId=1).response().result

Documentation
-------------

More documentation is available at http://bravado.readthedocs.org

Installation
------------

.. code-block:: bash

    # To install bravado with Synchronous Http Client only.
    $ pip install bravado

    # To install bravado with Synchronous and Asynchronous Http Client (RequestsClient and FidoClient).
    $ pip install bravado[fido]

Development
===========

Code is documented using `Sphinx <http://sphinx-doc.org/>`__.

`virtualenv <https://virtualenv.readthedocs.io/en/latest/>`__. is
recommended to keep dependencies and libraries isolated.

Setup
-----

.. code-block:: bash

    # Run tests
    tox

    # Install git pre-commit hooks
    tox -e pre-commit install

Contributing
------------

1. Fork it ( http://github.com/Yelp/bravado/fork )
2. Create your feature branch (``git checkout -b my-new-feature``)
3. Add your modifications
4. Commit your changes (``git commit -m "Add some feature"``)
5. Push to the branch (``git push origin my-new-feature``)
6. Create new Pull Request

License
-------

Copyright (c) 2013, Digium, Inc. All rights reserved.
Copyright (c) 2014-2015, Yelp, Inc. All rights reserved.

Easy ESIis licensed with a `BSD 3-Clause
License <http://opensource.org/licenses/BSD-3-Clause>`__.
