# -*- coding: utf-8 -*-
import typing
import warnings

if getattr(typing, 'TYPE_CHECKING', False):  # Needed to avoid cyclic import.
    from easyesi.client import CallableOperation  # pragma: no cover


def warn_for_deprecated_op(op):
    # type: (CallableOperation) -> None
    """Warn if requested operation has `deprecated` field flagged as True

    :param op: Operation object which contains operation id and operation spec
    :type op: :class:`easyesi.client.CallableOperation`
    """
    if op.op_spec.get('deprecated', False):
        message = "[DEPRECATED] {0} has now been deprecated. ".format(
            op.operation_id,
        )

        dep_date = op.op_spec.get('x-deprecated-date')
        if dep_date:
            message += "Deprecation Date: {0}. ".format(dep_date)

        rem_date = op.op_spec.get('x-removal-date')
        if rem_date:
            message += "Removal Date: {0}".format(rem_date)

        warnings.warn(message, Warning)
