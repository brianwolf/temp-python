from flask import Blueprint, jsonify, request
from flask_restplus import Resource, namespace
from logic.apps.config.rest import api
from logic.apps.example.errors.example_error import ExampleError
from logic.apps.example.routes.v1.dtos import example_dto
from logic.apps.example.services import example_service
from logic.libs.exception.exception import AppException

# blue_print = Blueprint('example', __name__, url_prefix='/api/v1')


# @blue_print.route('/examples', methods=['GET'])
# def get_example():

#     example = example_service.get_example()

#     return jsonify(example_dto.example_to_json(example))


# @blue_print.route('/examples', methods=['POST'])
# def post_example():

#     example = example_dto.json_to_example(request.json)

#     return jsonify(example_dto.example_to_json(example))


# @blue_print.route('/examples/errors/business', methods=['GET'])
# def get_error_business():

#     try:
#         1 / 0

#     except Exception as e:
#         raise AppException(
#             code=ExampleError.EXAMPLE_RANDOM_ERROR,
#             msj='BOOM...!!!',
#             exception=e
#         )

#     return '', 200


# @blue_print.route('/examples/errors/unknow', methods=['GET'])
# def get_error_unknows():

#     boom = 1 / 0

#     return '', 200


name_space = api.namespace('api/v1/examples', description='Ejemplos')


@name_space.route('')
class Examples(Resource):

    def get(self):
        example = example_service.get_example()
        return jsonify(example_dto.example_to_json(example))

    def post(self):
        example = example_dto.json_to_example(request.json)
        return jsonify(example_dto.example_to_json(example))


@name_space.route('/errors/unknow')
class ErrorUnknow(Resource):

    def get(self):
        boom = 1 / 0
        return '', 200


@name_space.route('/errors/business')
class ErrorBusiness(Resource):

    def get(self):
        try:
            1 / 0

        except Exception as e:
            raise AppException(
                code=ExampleError.EXAMPLE_RANDOM_ERROR,
                msj='BOOM...!!!',
                exception=e
            )

        return '', 200
