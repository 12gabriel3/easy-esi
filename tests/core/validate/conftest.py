# -*- coding: utf-8 -*-
from easy_esi_core.exception import SwaggerValidationError
from easy_esi_core.formatter import SwaggerFormat


def validate_email_address(email_address):
    if '@' not in email_address:
        raise SwaggerValidationError('dude, you need an @')


email_address_format = SwaggerFormat(
    format='email_address',
    to_wire=lambda x: x,
    to_python=lambda x: x,
    validate=validate_email_address,
    description='blah',
)
