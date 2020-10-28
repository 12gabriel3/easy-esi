# -*- coding: utf-8 -*-
from easyesi.client import CallableOperation
from easyesi.core.operation import Operation


def test_success(minimal_swagger_spec, getPetById_spec, request_dict):
    request_dict['url'] = '/pet/{petId}'
    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'get', getPetById_spec,
        ),
    )
    assert op.__doc__.startswith('[GET] Find pet by ID')
