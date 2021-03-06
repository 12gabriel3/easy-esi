# -*- coding: utf-8 -*-
import logging
import typing
from importlib import import_module

from easyesi.core.operation import Operation
from easyesi.core.response import IncomingResponse
from easyesi.response import EasyEsiResponseMetadata

try:
    from typing import Type
except ImportError:  # pragma: no cover
    # Python 3.5.0 / 3.5.1
    from typing_extensions import Type  # pragma: no cover


log = logging.getLogger(__name__)


CONFIG_DEFAULTS = {
    # See the constructor of :class:`easyesi.http_future.HttpFuture` for an
    # in depth explanation of what this means.
    'also_return_response': False,
    # Kill switch to disable returning fallback results even if provided.
    'disable_fallback_results': False,
    'response_metadata_class': 'easyesi.response.EasyEsiResponseMetadata',
}


EasyEsiConfig = typing.NamedTuple(
    'EasyEsiConfig',
    (
        ('also_return_response', bool),
        ('disable_fallback_results', bool),
        ('response_metadata_class', Type[EasyEsiResponseMetadata]),
    ),
)


def easyesi_config_from_config_dict(config_dict):
    # type: (typing.Mapping[str, typing.Any]) -> 'EasyEsiConfig'
    if config_dict is None:
        config_dict = {}
    easyesi_config = {key: value for key, value in config_dict.items() if key in EasyEsiConfig._fields}
    easyesi_config = dict(CONFIG_DEFAULTS, **easyesi_config)
    easyesi_config['response_metadata_class'] = _get_response_metadata_class(
        easyesi_config['response_metadata_class'],
    )
    return EasyEsiConfig(
        **easyesi_config
    )


class RequestConfig(object):

    also_return_response = False  # type: bool
    force_fallback_result = False  # type: bool

    # List of callbacks that are executed after the incoming response has been
    # validated and the swagger_result has been unmarshalled.
    #
    # The callback should expect two arguments:
    #   param : incoming_response
    #   type  : subclass of class:`core.response.IncomingResponse`
    #   param : operation
    #   type  : class:`core.operation.Operation`
    response_callbacks = []  # type: typing.List[typing.Callable[[IncomingResponse, Operation], None]]

    # options used to construct the request params
    connect_timeout = None  # type: typing.Optional[float]
    headers = {}  # type: typing.Mapping[str, str]
    use_msgpack = False  # type: bool
    timeout = None  # type: typing.Optional[float]

    # Extra options passed in that we don't know about
    additional_properties = {}  # type: typing.Mapping[str, typing.Any]

    def __init__(self, request_options, also_return_response_default):
        # type: (typing.Dict[str, typing.Any], bool) -> None
        request_options = request_options.copy()  # don't modify the original object
        self.also_return_response = also_return_response_default

        for key in list(request_options.keys()):
            if hasattr(self, key):
                setattr(self, key, request_options.pop(key))

        self.additional_properties = request_options


def _get_response_metadata_class(fully_qualified_class_str):
    # type: (str) -> typing.Type[EasyEsiResponseMetadata]

    class_to_import = _import_class(fully_qualified_class_str)
    if not class_to_import:
        return EasyEsiResponseMetadata

    if issubclass(class_to_import, EasyEsiResponseMetadata):
        return class_to_import

    log.warning(
        'easyesi configuration error: the metadata class \'%s\' does not extend '
        'EasyEsiResponseMetadata. Using default class instead.',
        fully_qualified_class_str,
    )
    return EasyEsiResponseMetadata


def _import_class(fully_qualified_class_str):
    # type: (str) -> typing.Optional[typing.Type]
    try:
        module_name, class_name = fully_qualified_class_str.rsplit('.', 1)
        return getattr(import_module(module_name), class_name)
    except (ImportError, AttributeError, ValueError) as e:
        log.warning(
            'Error while importing \'%s\': %s: %s',
            fully_qualified_class_str,
            type(e),
            str(e),
        )
        return None
