# -*- coding: utf-8 -*-
import pytest

from easyESI.core.exception import SwaggerMappingError
from easyESI.core.resource import convert_path_to_resource


def test_success():
    path_names = [
        '/pet',
        '/pet/findByStatus',
        '/pet/findByTags',
        '/pet/{petId}',
    ]
    for path_name in path_names:
        assert 'pet' == convert_path_to_resource(path_name)


def test_fails_on_empty_string():
    with pytest.raises(SwaggerMappingError) as excinfo:
        convert_path_to_resource('')
    assert 'name from path' in str(excinfo.value)


def test_fails_on_slash():
    with pytest.raises(SwaggerMappingError) as excinfo:
        convert_path_to_resource('/')
    assert 'name from path' in str(excinfo.value)
