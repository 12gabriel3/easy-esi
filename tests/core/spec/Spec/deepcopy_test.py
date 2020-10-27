# -*- coding: utf-8 -*-
from tests.core.conftest import check_object_deepcopy


def test_spec_instance_is_deep_copyable(petstore_spec):
    check_object_deepcopy(petstore_spec)
