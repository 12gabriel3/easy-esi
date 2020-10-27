# -*- coding: utf-8 -*-
from six import iterkeys
from six.moves.cPickle import dumps

from core.model import _from_pickleable_representation
from core.model import _to_pickleable_representation
from core.model import ModelDocstring


def test_ensure_pickleable_representation_is_pickleable(cat_type):
    pickleable_representation = _to_pickleable_representation('Cat', cat_type)
    # Ensures that the pickle.dump of the pickleable representation is pickleable
    # If the dumps call does not raise an exception then we were able to pickle
    # the model type
    dumps(pickleable_representation)


def test_ensure_that_get_model_type__from_pickleable_representation_returns_the_original_model(cat_type):
    # Ensures that the pickle.dump of the pickleable representation is pickleable
    # If the dumps call does not raise an exception then we were able to pickle
    # the model type
    reconstructed_model_type = _from_pickleable_representation(
        model_pickleable_representation=_to_pickleable_representation('Cat', cat_type),
    )
    assert reconstructed_model_type.__name__ == 'Cat'

    def is_the_same(attr_name):
        if attr_name == '_swagger_spec':
            return cat_type._swagger_spec.is_equal(reconstructed_model_type._swagger_spec)
        elif attr_name == '__doc__':
            return (
                isinstance(cat_type.__dict__[attr_name], ModelDocstring) and
                isinstance(reconstructed_model_type.__dict__[attr_name], ModelDocstring)
            )
        elif attr_name == '_abc_impl':
            # _abc_impl is of type builtins._abc_data which is not really comparable. So we'll ignore it
            return True
        else:
            return cat_type.__dict__[attr_name] == reconstructed_model_type.__dict__[attr_name]

    assert [
        attribute_name
        for attribute_name in iterkeys(cat_type.__dict__)
        if not is_the_same(attribute_name)
    ] == []
