import os
from flask_testing import TestCase
from tests.resources.test_app import create_app
from flask import Blueprint, jsonify
from flask_swagger_generator.generators import Generator
from flask_swagger_generator.specifiers import SwaggerVersion
from flask_swagger_generator.utils import ParameterType, SecurityType

from marshmallow import Schema, fields

app = create_app()

generator = Generator.of(SwaggerVersion.VERSION_THREE)
blueprint = Blueprint('objects', __name__)

# object_id_parameter = generator.create_parameter(parameter_type=ParameterType.PATH, name='object_id')

class ObjectSerializer(Schema):
    id = fields.Integer()
    name = fields.String()


class ObjectDeserializer(Schema):
    id = fields.Integer()
    name = fields.String()


# schema_one = generator.create_schema(['id', 'name'])
# schema_two = generator.create_schema({'id': 10, 'name': 'test_object'})
# schema_three = generator.create_schema(ObjectDeserializer())


# @generator.response(status_code=200, schema={'id': 10, 'name': 'test_object'})
# @generator.parameter(
#     parameter_type=ParameterType.PATH, name="object_id", description="The ID of the object to retrieve", required=True
# )
# @generator.security(SecurityType.BEARER_AUTH)
@blueprint.route('/objects/<int:object_id>', methods=['GET'])
def retrieve_object(object_id, child_id):
    return jsonify({'objects': []}), 200


# @generator.response(204, schema_one)
# @generator.parameter(
#     parameter_type=ParameterType.PATH, name="object_id", description="The ID of the object to retrieve", required=True
# )
# @generator.security(SecurityType.BEARER_AUTH)
@blueprint.route('/objects/<int:object_id>', methods=['DELETE'])
def delete_object(object_id):
    return jsonify({'objects': []}), 200


@generator.request_body(ObjectDeserializer)
@blueprint.route('/objects/<int:object_id>', methods=['PUT'])
def update_object(object_id):
    pass

#
# @generator.response(status_code=201, schema={'id': 10, 'name': 'test_object'})
# @generator.request_body({'id': 10, 'name': 'test_object'})
# @blueprint.route('/objects/<int:object_id>', methods=['GET'])
# def create_object(object_id):
#     return jsonify({'objects': []}), 200


app.register_blueprint(blueprint)


class AppTestBase(TestCase):

    def setUp(self) -> None:
        super(AppTestBase, self).setUp()

    def create_app(self):
        return app

    def tearDown(self):
        super(AppTestBase, self).tearDown()

    def test(self):
        generator.generate_swagger(
            self.app, destination_path='resources/generated.yaml'
        )
        # self.assertEqual(3, len(generator.specifier.endpoints.keys()))
        # self.assertEqual(2, len(generator.specifier.responses.keys()))
        # self.assertEqual(2, len(generator.specifier.parameters.keys()))
        # self.assertEqual(2, len(generator.specifier.security_schemas.keys()))
