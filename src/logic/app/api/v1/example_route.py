from datetime import datetime

from flask import Blueprint, jsonify, render_template, request
from logic.app.api.v1.dto import example_dto
from logic.app.error.example_error import ExampleError
from logic.app.model.example import Example
from logic.app.service.produce import example_service
from logic.libs.exception.exception import AppException

blue_print = Blueprint('example', __name__, url_prefix='/api/v1')


@blue_print.route('/examples', methods=['GET'])
def get_example():

    example = example_service.get_example()

    return jsonify(example_dto.example_to_json(example))


@blue_print.route('/examples', methods=['POST'])
def post_example():

    example = example_dto.json_to_example(request.json)

    return jsonify(example_dto.example_to_json(example))


@blue_print.route('/examples/errors/business', methods=['GET'])
def get_error_business():

    try:
        1 / 0

    except Exception as e:
        raise AppException(
            code=ExampleError.EXAMPLE_RANDOM_ERROR,
            msj='BOOM...!!!',
            exception=e
        )

    return '', 200


@blue_print.route('/examples/errors/unknow', methods=['GET'])
def get_error_unknows():

    boom = 1 / 0

    return '', 200
