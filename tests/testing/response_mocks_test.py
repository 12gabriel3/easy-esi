# -*- coding: utf-8 -*-
import inspect

import mock
import pytest

from easyesi.config import RequestConfig
from easyesi.core.response import IncomingResponse
from easyesi.exception import HTTPServerError
from easyesi.http_future import HttpFuture
from easyesi.response import EasyEsiResponseMetadata
from easyesi.testing.response_mocks import EasyEsiResponseMock
from easyesi.testing.response_mocks import FallbackResultEasyEsiResponseMock


@pytest.fixture
def mock_result():
    return mock.NonCallableMock(name='mock result')


@pytest.fixture
def mock_metadata():
    return EasyEsiResponseMetadata(
        incoming_response=IncomingResponse(),
        swagger_result=None,
        start_time=5,
        request_end_time=6,
        handled_exception_info=None,
        request_config=RequestConfig({}, also_return_response_default=False),
    )


def test_response_mock_signatures():
    """Make sure the mocks' __call__ methods have the same signature as HttpFuture.response"""
    response_signature = inspect.getargspec(HttpFuture.response)

    assert inspect.getargspec(EasyEsiResponseMock.__call__) == response_signature
    assert inspect.getargspec(FallbackResultEasyEsiResponseMock.__call__) == response_signature


def test_easyesi_response(mock_result):
    response_mock = EasyEsiResponseMock(mock_result)
    response = response_mock()

    assert response.result is mock_result
    assert isinstance(response.metadata, EasyEsiResponseMetadata)
    assert response.metadata._swagger_result is mock_result


def test_easyesi_response_custom_metadata(mock_result, mock_metadata):
    response_mock = EasyEsiResponseMock(mock_result, metadata=mock_metadata)
    response = response_mock()

    assert response.metadata is mock_metadata


def test_fallback_result_easyesi_response(mock_result):
    # type: (mock.NonCallableMagicMock) -> None
    response_mock = FallbackResultEasyEsiResponseMock()
    response = response_mock(fallback_result=mock_result)

    assert response.result is mock_result
    assert isinstance(response.metadata, EasyEsiResponseMetadata)
    assert response.metadata._swagger_result is mock_result


def test_fallback_result_easyesi_response_callable(mock_result):
    exception = HTTPServerError(mock.Mock('incoming response', status_code=500))

    def handle_fallback_result(exc):
        assert exc is exception
        return mock_result

    response_mock = FallbackResultEasyEsiResponseMock(exception)
    response = response_mock(fallback_result=handle_fallback_result)

    assert response.result is mock_result
    assert isinstance(response.metadata, EasyEsiResponseMetadata)
    assert response.metadata._swagger_result is mock_result


def test_fallback_result_easyesi_response_custom_metadata(mock_result, mock_metadata):
    response_mock = FallbackResultEasyEsiResponseMock(metadata=mock_metadata)
    response = response_mock(fallback_result=mock_result)

    assert response.metadata is mock_metadata
    assert response.metadata._swagger_result is mock_result


def test_fallback_result_response_without_fallback_result():
    response_mock = FallbackResultEasyEsiResponseMock()
    with pytest.raises(AssertionError):
        response_mock()
