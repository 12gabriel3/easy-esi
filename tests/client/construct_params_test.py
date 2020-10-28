# -*- coding: utf-8 -*-
import pytest
from mock import patch

from easyesi.client import CallableOperation
from easyesi.client import construct_params
from easyesi.core.exception import SwaggerMappingError
from easyesi.core.operation import Operation


@patch('easyesi.client.marshal_param')
def test_simple(
    mock_marshal_param, minimal_swagger_spec, getPetById_spec,
    request_dict,
):
    request_dict['url'] = '/pet/{petId}'
    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'get', getPetById_spec,
        ),
    )
    construct_params(op, request_dict, op_kwargs={'petId': 34, 'api-key': 'foo'})
    assert 2 == mock_marshal_param.call_count


@patch('easyesi.client.marshal_param')
def test_no_params(mock_marshal_param, minimal_swagger_spec, request_dict):
    get_op = minimal_swagger_spec.spec_dict['paths']['/pet/{petId}']['get']
    del get_op['parameters'][0]
    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'get', {},
        ),
    )
    construct_params(op, request_dict, op_kwargs={})
    assert 0 == mock_marshal_param.call_count
    assert request_dict == {
        'params': {},
        'headers': {},
    }


def test_extra_parameter_error(minimal_swagger_spec, request_dict):
    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'get', {},
        ),
    )
    with pytest.raises(SwaggerMappingError) as excinfo:
        construct_params(op, request_dict, op_kwargs={'extra_param': 'bar'})
    assert 'does not have parameter' in str(excinfo.value)


def test_required_parameter_missing(
        minimal_swagger_spec, getPetById_spec, request_dict,
):
    request_dict['url'] = '/pet/{petId}'
    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'get', getPetById_spec,
        ),
    )
    with pytest.raises(SwaggerMappingError) as excinfo:
        construct_params(op, request_dict, op_kwargs={})
    assert 'required parameter' in str(excinfo.value)


@patch('easyesi.client.marshal_param')
def test_validate_header_parameter_from_request_options(
        mock_marshal_param, minimal_swagger_spec, getPetById_spec, request_dict,
):
    request_dict['url'] = '/pet/{petId}'
    request_dict['headers']['api-key'] = 'api-key'

    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'delete', getPetById_spec,
        ),
    )
    construct_params(op, request_dict, op_kwargs={'petId': 1})
    assert 2 == mock_marshal_param.call_count


@patch('easyesi.client.marshal_param')
def test_non_required_parameter_with_default_used(
        mock_marshal_param, minimal_swagger_spec, getPetById_spec,
        request_dict,
):

    del getPetById_spec['parameters'][0]['required']
    getPetById_spec['parameters'][0]['default'] = 99
    request_dict['url'] = '/pet/{petId}'
    op = CallableOperation(
        Operation.from_spec(
            minimal_swagger_spec, '/pet/{petId}', 'get', getPetById_spec,
        ),
    )
    construct_params(op, request_dict, op_kwargs={'api-key': 'foo'})
    assert 2 == mock_marshal_param.call_count
