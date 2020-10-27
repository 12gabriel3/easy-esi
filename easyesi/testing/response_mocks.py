# -*- coding: utf-8 -*-
import typing

from typing_extensions import overload  # typing.overload won't work on Python 3.5.0/3.5.1

from easyesi.config import RequestConfig
from easyesi.core import IncomingResponse
from easyesi.exception import EasyEsiTimeoutError
from easyesi.http_future import _SENTINEL
from easyesi.http_future import FALLBACK_EXCEPTIONS
from easyesi.http_future import SENTINEL
from easyesi.response import EasyEsiResponse
from easyesi.response import EasyEsiResponseMetadata


T = typing.TypeVar('T')


class IncomingResponseMock(IncomingResponse):
    def __init__(self, status_code, **kwargs):
        self.headers = {}  # type: typing.Mapping[str, str]
        self.status_code = status_code
        for name, value in kwargs.items():
            setattr(self, name, value)


class EasyEsiResponseMock(typing.Generic[T]):
    """Class that behaves like the :meth:`.HttpFuture.response` method as well as a :class:`.EasyEsiResponse`.
    Please check the documentation for further information.
    """

    def __init__(self, result, metadata=None):
        # type: (T, typing.Optional[EasyEsiResponseMetadata[T]]) -> None
        self._result = result
        if metadata:
            self._metadata = metadata
        else:
            self._metadata = EasyEsiResponseMetadata(
                incoming_response=IncomingResponseMock(status_code=200),
                swagger_result=self._result,
                start_time=1528733800,
                request_end_time=1528733801,
                handled_exception_info=None,
                request_config=RequestConfig({}, also_return_response_default=False),
            )

    def __call__(
        self,
        timeout=None,  # type: typing.Optional[float]
        fallback_result=SENTINEL,  # type: typing.Union[_SENTINEL, T, typing.Callable[[BaseException], T]]  # noqa
        exceptions_to_catch=FALLBACK_EXCEPTIONS,  # type: typing.Tuple[typing.Type[BaseException], ...]
    ):
        # type: (...) -> EasyEsiResponse[T]
        return self  # type: ignore

    @property
    def result(self):
        return self._result

    @property
    def metadata(self):
        return self._metadata


class FallbackResultEasyEsiResponseMock(object):
    """Class that behaves like the :meth:`.HttpFuture.response` method as well as a :class:`.EasyEsiResponse`.
    It will always call the ``fallback_result`` callback that's passed to the ``response()`` method.
    Please check the documentation for further information.
    """

    def __init__(self, exception=EasyEsiTimeoutError(), metadata=None):
        # type: (BaseException, typing.Optional[EasyEsiResponseMetadata]) -> None
        self._exception = exception
        if metadata:
            self._metadata = metadata
        else:
            self._metadata = EasyEsiResponseMetadata(
                incoming_response=IncomingResponse(),
                swagger_result=None,  # we're going to set it later
                start_time=1528733800,
                request_end_time=1528733801,
                handled_exception_info=[self._exception.__class__, self._exception, 'Traceback'],
                request_config=RequestConfig({}, also_return_response_default=False),
            )

    @overload
    def __call__(
        self,
        timeout=None,  # type: typing.Optional[float]
        fallback_result=T,  # type: T
        exceptions_to_catch=FALLBACK_EXCEPTIONS,  # type: typing.Tuple[typing.Type[BaseException], ...]
    ):
        # type: (...) -> EasyEsiResponse[T]
        pass

    @overload  # noqa: F811
    def __call__(
        self,
        timeout=None,  # type: typing.Optional[float]
        fallback_result=lambda x: None,  # typing.Callable[[BaseException], T]
        exceptions_to_catch=FALLBACK_EXCEPTIONS,  # type: typing.Tuple[typing.Type[BaseException], ...]
    ):
        # type: (...) -> EasyEsiResponse[T]
        pass

    def __call__(  # noqa: F811
        self,
        timeout=None,  # type: typing.Optional[float]
        fallback_result=SENTINEL,  # type: typing.Union[_SENTINEL, T, typing.Callable[[BaseException], T]]  # noqa
        exceptions_to_catch=FALLBACK_EXCEPTIONS,  # type: typing.Tuple[typing.Type[BaseException], ...]
    ):
        # type: (...) -> EasyEsiResponse[T]
        assert not isinstance(fallback_result, _SENTINEL), 'You\'re using FallbackResultEasyEsiResponseMock without' \
            ' a fallback_result. Either provide one or use EasyEsiResponseMock.'
        self._fallback_result = fallback_result(self._exception) if callable(fallback_result) else fallback_result
        self._metadata._swagger_result = self._fallback_result
        return self  # type: ignore

    @property
    def result(self):
        return self._fallback_result

    @property
    def metadata(self):
        return self._metadata
