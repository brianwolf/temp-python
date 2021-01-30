"""
Rest
----
1.0.0

Configura el app de Flask para cargar blueprints dinamicamente, agregar JSON decoders que sigan un estandar, 
agregar handlers para manejo automatico de errores, entre otros.
"""
from flask import Flask
from logic.libs.exception.exception import AppException, UnknownException
from logic.libs.logger.logger import logger
from logic.libs.rest.src import config
from logic.libs.rest.src.json import JSONEncoderCustom
from werkzeug.exceptions import HTTPException


def load_generic_error_handler(app: Flask):
    """
    Carga el handler de error basico para manejo de AppExceptions y excepciones comunes
    """
    @app.errorhandler(HTTPException)
    def handle_exception(httpe):
        return '', httpe.code

    @app.errorhandler(AppException)
    def handle_business_exception(ae: AppException):
        logger().warning(ae.to_json())
        return ae.to_json(), config.HTTP_STATUS_BUSINESS_ERROR

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        logger().exception(e)
        return UnknownException(e).to_json(), config.HTTP_STATUS_UNKNOW_ERROR


def load_generic_json_coders(app: Flask):
    """
    Carga el json encoder y decoder genericos
    """
    app.json_encoder = JSONEncoderCustom
