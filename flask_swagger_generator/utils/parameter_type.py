from enum import Enum
from flask_swagger_generator.exceptions import SwaggerGeneratorException


class ParameterType(Enum):
    """
    Class SwaggerVersion: Enum for types of swagger version
    """

    PATH = 'PATH'
    QUERY = 'QUERY'
    HEADER = 'HEADER'
    FORMDATA = 'FORMDATA'
    BODY = 'BODY'

    @staticmethod
    def from_string(value: str):

        if not isinstance(value, str):
            raise SwaggerGeneratorException(
                "Could not convert non string value to a parameter type"
            )
        if value.lower() == 'path':
            return ParameterType.PATH
        elif value.lower() == 'query':
            return ParameterType.QUERY
        elif value.lower() == 'header':
            return ParameterType.HEADER
        elif value.lower() == 'formdata':
            return ParameterType.FORMDATA
        elif value.lower() == 'body':
            return ParameterType.BODY
        else:
            raise SwaggerGeneratorException(
                f'Could not convert value {value} to a parameter type'
            )

    def equals(self, other):

        if isinstance(other, Enum):
            return self.value == other.value
        try:
            data_base_type = ParameterType.from_string(other)
            return data_base_type == self
        except SwaggerGeneratorException:
            pass

        return other == self.value
