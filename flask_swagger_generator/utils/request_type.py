from enum import Enum
from flask_swagger_generator.exceptions import SwaggerGeneratorException


class RequestType(Enum):
    """
    Class RequestType: Enum for types of requests
    """

    POST = 'post'
    GET = 'get'
    DELETE = 'delete'
    PUT = 'put'

    @staticmethod
    def from_string(value: str):

        if not isinstance(value, str):
            raise SwaggerGeneratorException(
                "Could not convert non string value to a request type"
            )
        if value.lower() == 'post':
            return RequestType.POST
        elif value.lower() == 'get':
            return RequestType.GET
        elif value.lower() == 'delete':
            return RequestType.DELETE
        elif value.lower() == 'put':
            return RequestType.PUT
        else:
            raise SwaggerGeneratorException(
                f'Could not convert value {value} to a request type'
            )

    def equals(self, other):

        if isinstance(other, Enum):
            return self.value == other.value
        try:
            data_base_type = RequestType.from_string(other)
            return data_base_type == self
        except SwaggerGeneratorException:
            pass

        return other == self.value
