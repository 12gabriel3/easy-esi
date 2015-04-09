from bravado.core.operation import Operation
from bravado.core.spec import Spec


def test_returns_operation_id_from_operation_spec():
    spec = Spec(spec_dict={})
    operation_spec = {'operationId': 'getPetById'}
    operation = Operation(spec, '/pet/{petId}', 'get', operation_spec)
    assert 'getPetById' == operation.operation_id


def test_returns_generated_operation_id_when_missing_from_operation_spec():
    spec = Spec(spec_dict={})
    operation_spec = {}
    operation = Operation(spec, '/pet', 'get', operation_spec)
    assert 'get_pet' == operation.operation_id


def test_returns_generated_operation_id_with_path_parameters():
    spec = Spec(spec_dict={})
    operation_spec = {}
    operation = Operation(spec, '/pet/{petId}', 'get', operation_spec)
    assert 'get_pet_petId' == operation.operation_id
