from flask import Blueprint
from logic.libs.exception.exception import AppException, UnknownException
from logic.libs.logger.logger import logger
from werkzeug.exceptions import HTTPException

# error_handler_bp = Blueprint('handlers', __name__)


# @error_handler_bp.app_errorhandler(HTTPException)
# def handle_exception(httpe):
#     return '', httpe.code


# @error_handler_bp.app_errorhandler(Exception)
# def handle_exception(e: Exception):
#     logger().exception(e)
#     return UnknownException(e).rest_response()


# @error_handler_bp.app_errorhandler(AppException)
# def handle_business_exception(ae: AppException):
#     logger().warning(ae.to_json())
#     return ae.rest_response()


def registrar(error_handler_bp):
    @error_handler_bp.errorhandler(HTTPException)
    def handle_exception(httpe):
        return '', httpe.code

    @error_handler_bp.errorhandler(AppException)
    def handle_business_exception(ae: AppException):
        logger().warning(ae.to_json())
        # return ae.rest_response()
        return {'message': 'What you want'}, 400
        
    @error_handler_bp.errorhandler(Exception)
    def handle_exception(e: Exception):
        logger().exception(e)
        return UnknownException(e).rest_response()

