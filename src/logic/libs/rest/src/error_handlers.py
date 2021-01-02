from flask import Blueprint
from werkzeug.exceptions import HTTPException

from logic.libs.exception.exception import AppException, UnknownException
from logic.libs.logger.logger import logger

error_handler_bp = Blueprint('handlers', __name__)


@error_handler_bp.app_errorhandler(HTTPException)
def handle_exception(httpe):
    return '', httpe.code


@error_handler_bp.app_errorhandler(Exception)
def handle_exception(e: Exception):
    logger().exception(e)
    return UnknownException(e).rest_response()


@error_handler_bp.app_errorhandler(AppException)
def handle_business_exception(ae: AppException):
    logger().warning(ae.to_json())
    return ae.rest_response()
