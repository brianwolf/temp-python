from flask import jsonify, request
from flask_restplus import Resource
from logic.apps.config.rest import api
from logic.apps.errors.example_error import ExampleError
from logic.apps.routes.v1.dtos import example_dto
from logic.apps.services import example_service
from logic.libs.exception.exception import AppException

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
