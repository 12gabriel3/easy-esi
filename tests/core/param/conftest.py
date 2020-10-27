# -*- coding: utf-8 -*-
import pytest

from core.spec import Spec


@pytest.fixture
def empty_swagger_spec():
    return Spec(spec_dict={})
