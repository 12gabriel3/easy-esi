# -*- coding: utf-8 -*-
import typing

from core.operation import Operation
from easyESI.config import RequestConfig
from easyESI.http_future import HttpFuture

APP_FORM = 'application/x-www-form-urlencoded'
MULT_FORM = 'multipart/form-data'


class HttpClient(object):
    """Interface for a minimal HTTP client that can retrieve Swagger specs
    and perform HTTP calls to fulfill a Swagger operation.
    """

    def request(
        self,
        request_params,  # type: typing.MutableMapping[str, typing.Any]
        operation=None,  # type: typing.Optional[Operation]
        request_config=None,  # type: typing.Optional[RequestConfig]
    ):
        # type: (...) -> HttpFuture
        """
        :param request_params: complete request data. e.g. url, method,
            headers, body, params, connect_timeout, timeout, etc.
        :type request_params: dict
        :param operation: operation that this http request is for. Defaults
            to None - in which case, we're obviously just retrieving a Swagger
            Spec.
        :type operation: :class:`core.operation.Operation`
        :param RequestConfig request_config: Per-request config that is passed to
            :class:`easyESI.http_future.HttpFuture`.

        :returns: HTTP Future object
        :rtype: :class: `core.http_future.HttpFuture`
        """
        raise NotImplementedError(
            u"%s: Method not implemented", self.__class__.__name__,
        )

    def __repr__(self):
        # type: () -> str
        return "{0}()".format(type(self))
