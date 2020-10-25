# -*- coding: utf-8 -*-
import mock

from easy_esi.config import RequestConfig
from easy_esi.response import EasyEsiResponseMetadata


def test_response_metadata_times():
    with mock.patch('monotonic.monotonic', return_value=11):
        metadata = EasyEsiResponseMetadata(
            incoming_response=None,
            swagger_result=None,
            start_time=5,
            request_end_time=10,
            handled_exception_info=None,
            request_config=RequestConfig({}, also_return_response_default=False),
        )  # type: EasyEsiResponseMetadata[None]

    assert metadata.elapsed_time == 6
    assert metadata.request_elapsed_time == 5
