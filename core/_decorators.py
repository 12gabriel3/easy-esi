# -*- coding: utf-8 -*-
import typing

from core import schema
from core._compat import wraps
from core.exception import SwaggerMappingError
from core.util import memoize_by_id
from core.util import RecursiveCallException


if getattr(typing, 'TYPE_CHECKING', False):
    from core.spec import Spec
    from core._compat_typing import JSONDict
    from core._compat_typing import Func


@memoize_by_id
def handle_null_value(swagger_spec, object_schema, is_nullable=False, is_marshaling_operation=False):
    # type: (Spec, JSONDict, bool, bool) -> typing.Callable[[Func], Func]
    # TODO: remove is_nullable support once https://github.com/Yelp/easy-esi-core/issues/335 is addressed
    """
    Function wrapper that performs some check to the wrapped function parameter.

    In case the parameter is None the decorator ensures that, according to object schema,
    the default value is used or that the null value is properly handled.

    NOTES:
     * the decorator is meant to be used in core.marshal and core.unmarshal modules.
     * the decorator could be used as wrapper of functions that accept a single value as parameter.
       Such value will be used for the checks mentioned above
     * nullable parameter is needed to ensure that x-nullable is propagated in the case it is defined
       as sibling in a reference object (ie. `{'x-nullable': True, '$ref': '#/definitions/something'}`)

    """
    default_value = schema.get_default(swagger_spec, object_schema)
    is_nullable = is_nullable or schema.is_prop_nullable(swagger_spec, object_schema)

    def external_wrapper(func):
        # type: (Func) -> Func
        @wraps(func)
        def wrapper(value):
            # type: (typing.Any) -> typing.Any
            if value is None:
                value = default_value

                if value is None:
                    if is_nullable:
                        return None
                    else:
                        raise SwaggerMappingError(
                            'Spec {0} is a required value'.format(object_schema),
                        )
                elif is_marshaling_operation:
                    return value
            return func(value)

        return wrapper

    return external_wrapper


def wrap_recursive_call_exception(func):
    # type: (Func) -> Func
    """
    The core.marshaling and core.unmarshaling modules might
    take advantage of caching the return value of determined function calls.

    In the case of higher level function, so functions that return functions
    that are memoized it is necessary to deal with the fact that caching
    them on the first time might not be possible (due to RecursiveCallException).

    In such case the decorator takes care of returning a new callable, with
    the same signature of the original function, that will re-execute the original
    function in the hope that a later execution will not result into a
    recursive-call that makes caching not feasible.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # type: (typing.Any, typing.Any) -> typing.Any
        try:
            return func(*args, **kwargs)
        except RecursiveCallException:
            return lambda *new_args, **new_kawrgs: func(*args, **kwargs)(*new_args, **new_kawrgs)

    return wrapper
