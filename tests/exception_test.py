# -*- coding: utf-8 -*-
import pytest
from requests.models import Response

from easyESI.exception import HTTPClientError
from easyESI.exception import HTTPError
from easyESI.exception import HTTPForbidden
from easyESI.exception import HTTPInternalServerError
from easyESI.exception import HTTPMovedPermanently
from easyESI.exception import HTTPRedirection
from easyESI.exception import HTTPServerError
from easyESI.exception import HTTPServiceUnavailable
from easyESI.exception import make_http_exception
from easyESI.requests_client import RequestsResponseAdapter


@pytest.fixture
def response_500():
    requests_response = Response()
    requests_response.status_code = 500
    requests_response.reason = "Server Error"
    return requests_response


def test_response_only(response_500):
    incoming_response = RequestsResponseAdapter(response_500)
    assert str(HTTPError(incoming_response)) == '500 Server Error'


def test_response_and_message(response_500):
    incoming_response = RequestsResponseAdapter(response_500)
    actual = str(HTTPError(incoming_response, message="Kaboom"))
    assert actual == '500 Server Error: Kaboom'


def test_response_and_swagger_result(response_500):
    incoming_response = RequestsResponseAdapter(response_500)
    actual = str(HTTPError(incoming_response, swagger_result={'msg': 'Kaboom'}))
    assert actual == "500 Server Error: {'msg': 'Kaboom'}"


def test_response_and_message_and_swagger_result(response_500):
    incoming_response = RequestsResponseAdapter(response_500)
    actual = str(
        HTTPError(
            incoming_response,
            message="Holy moly!",
            swagger_result={'msg': 'Kaboom'},
        ),
    )
    assert actual == "500 Server Error: Holy moly!: {'msg': 'Kaboom'}"


def test_make_http_exception(response_500):
    incoming_response = RequestsResponseAdapter(response_500)
    exc = make_http_exception(
        incoming_response,
        message="Holy moly!",
        swagger_result={'msg': 'Kaboom'},
    )
    assert isinstance(exc, HTTPError)
    assert isinstance(exc, HTTPServerError)
    assert type(exc) == HTTPInternalServerError
    assert str(exc) == "500 Server Error: Holy moly!: {'msg': 'Kaboom'}"


@pytest.mark.parametrize(
    'status_code, expected_type',
    [
        [301, HTTPMovedPermanently],
        [399, HTTPRedirection],
        [403, HTTPForbidden],
        [499, HTTPClientError],
        [503, HTTPServiceUnavailable],
        [599, HTTPServerError],
        [600, HTTPError],
    ],
)
def test_make_http_exception_type(status_code, expected_type):
    requests_response = Response()
    requests_response.status_code = status_code
    requests_response.reason = "Womp Error"
    exc = make_http_exception(
        RequestsResponseAdapter(requests_response),
    )
    assert type(exc) == expected_type
