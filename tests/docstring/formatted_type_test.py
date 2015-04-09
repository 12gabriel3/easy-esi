import pytest

from bravado_core.exception import SwaggerMappingError
from bravado_core.docstring import formatted_type


def test_type_only():
    schema_obj = {
        'type': 'integer',
    }
    assert 'integer' == formatted_type(schema_obj)


def test_format_and_type():
    schema_obj = {
        'type': 'integer',
        'format': 'int64',
    }
    assert 'integer:int64' == formatted_type(schema_obj)


def test_array():
    schema_obj = {
        'type': 'array',
        'items': {
            'type': 'string',
        }
    }
    assert 'array:string' == formatted_type(schema_obj)


def test_ref():
    schema_obj = {
        '$ref': '#/definitions/Foo',
    }
    assert '#/definitions/Foo' == formatted_type(schema_obj)


def test_missing_type_raises_error():
    with pytest.raises(SwaggerMappingError) as excinfo:
        formatted_type({'TyP3': 'string'})
    assert 'No proper type' in str(excinfo.value)
