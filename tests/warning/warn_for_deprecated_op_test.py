# -*- coding: utf-8 -*-
from mock import Mock
from mock import patch

from easyESI.client import CallableOperation
from easyESI.warning import warn_for_deprecated_op


@patch('easyESI.warning.warnings.warn')
def test_warn(mock_warn):
    op_spec = {
        'deprecated': True,
        'x-deprecated-date': 'foo',
        'x-removal-date': 'bar',
    }
    op = Mock(spec=CallableOperation, operation_id='bla', op_spec=op_spec)
    warn_for_deprecated_op(op)
    mock_warn.assert_called_once_with(
        '[DEPRECATED] bla has now been deprecated.'
        ' Deprecation Date: foo. Removal Date: bar', Warning,
    )


@patch('easyESI.warning.warnings.warn')
def test_no_warn_if_false(mock_warn):
    op_spec = {'deprecated': False}
    op = Mock(spec=CallableOperation, operation_id='bla', op_spec=op_spec)
    warn_for_deprecated_op(op)
    assert not mock_warn.called


@patch('easyESI.warning.warnings.warn')
def test_no_warn_if_deprecate_flag_not_present(mock_warn):
    op = Mock(spec=CallableOperation, operation_id='bla', op_spec={})
    warn_for_deprecated_op(op)
    assert not mock_warn.called
