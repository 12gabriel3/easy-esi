# -*- coding: utf-8 -*-
import pytest

from easyesi.core.spec import Spec


@pytest.fixture
def empty_swagger_spec():
    return Spec(spec_dict={})
