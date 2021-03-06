# -*- coding: utf-8 -*-
import pytest

from easyesi.client import SwaggerClient
from easyesi.core.spec import Spec


@pytest.fixture
def petstore_client(petstore_dict):
    return SwaggerClient.from_spec(petstore_dict)


@pytest.fixture
def request_dict():
    return {
        'params': {},
        'headers': {},
    }


@pytest.fixture
def getPetById_spec(petstore_dict):
    return petstore_dict['paths']['/pet/{petId}']['get']


@pytest.fixture
def minimal_swagger_dict(getPetById_spec):
    spec_dict = {
        'paths': {
            '/pet/{petId}': {
                'get': getPetById_spec,
            },
        },
        'securityDefinitions': {
            'api-key': {
                'type': 'apiKey',
                'name': 'api-key',
                'in': 'header',
            },
        },
    }
    return spec_dict


@pytest.fixture
def minimal_swagger_spec(minimal_swagger_dict):
    spec = Spec(minimal_swagger_dict)
    spec.api_url = 'http://localhost/'
    return spec
