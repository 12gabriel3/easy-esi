# -*- coding: utf-8 -*-
import pytest
from easy_esi_core.response import IncomingResponse
from mock import Mock

from easy_esi.exception import HTTPError
from easy_esi.http_future import raise_on_unexpected


def test_5XX():
    http_response = Mock(spec=IncomingResponse, status_code=500)
    with pytest.raises(HTTPError) as excinfo:
        raise_on_unexpected(http_response)
    assert excinfo.value.response.status_code == 500


def test_non_5XX():
    http_response = Mock(spec=IncomingResponse, status_code=200)
    # no error raises == success
    raise_on_unexpected(http_response)
