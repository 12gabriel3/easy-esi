# -*- coding: utf-8 -*-
import pytest

from easyESI.core.exception import SwaggerMappingError
from easyESI.core.schema import handle_null_value


def test_default(empty_swagger_spec):
    spec = {
        'type': 'integer',
        'default': 42,
    }

    assert 42 == handle_null_value(empty_swagger_spec, spec)


def test_nullable(empty_swagger_spec):
    spec = {
        'type': 'integer',
        'x-nullable': True,
    }

    assert None is handle_null_value(empty_swagger_spec, spec)


def test_raise(empty_swagger_spec):
    spec = {
        'type': 'integer',
    }

    with pytest.raises(SwaggerMappingError):
        handle_null_value(empty_swagger_spec, spec)
