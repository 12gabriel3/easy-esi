# -*- coding: utf-8 -*-
import mock
import pytest

from easy_esi.http_future import FutureAdapter


@pytest.fixture
def mock_future_adapter():
    return mock.Mock(
        spec=FutureAdapter,
        timeout_errors=None,
        connection_errors=None,
    )
