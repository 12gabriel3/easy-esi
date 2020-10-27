# -*- coding: utf-8 -*-
from mock import Mock
from mock import patch

from easyesi.core.operation import Operation
from easyesi.core.response import OutgoingResponse
from easyesi.core.response import validate_response
from easyesi.core.spec import Spec


@patch('easyesi.core.response.validate_response_headers')
@patch('easyesi.core.response.validate_response_body')
def test_skip_when_configured_to_not_validate(mock_validate_response_body, mock_validate_response_headers):
    swagger_spec = Mock(spec=Spec, config={'validate_responses': False})
    op = Mock(spec=Operation, swagger_spec=swagger_spec)
    response = Mock(spec=OutgoingResponse)
    validate_response({'description': 'blah'}, op, response)
    assert mock_validate_response_body.call_count == 0
    assert mock_validate_response_headers.call_count == 0


@patch('easyesi.core.response.validate_response_headers')
@patch('easyesi.core.response.validate_response_body')
def test_validate_when_configured_validate(mock_validate_response_body, mock_validate_response_headers):
    swagger_spec = Mock(spec=Spec, config={'validate_responses': True})
    op = Mock(spec=Operation, swagger_spec=swagger_spec)
    response = Mock(spec=OutgoingResponse)
    validate_response({'description': 'blah'}, op, response)
    assert mock_validate_response_body.call_count == 1
    assert mock_validate_response_headers.call_count == 1
