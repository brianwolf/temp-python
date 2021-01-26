"""
Rest
----
1.0.0

Configura el app de Flask para cargar blueprints dinamicamente, agregar JSON decoders que sigan un estandar, 
agregar handlers para manejo automatico de errores, entre otros.
"""
from importlib.util import module_from_spec, spec_from_file_location

from flask import Flask
from logic.libs.exception.exception import AppException, UnknownException
from logic.libs.logger.logger import logger
from logic.libs.rest.src import config
from logic.libs.rest.src.blue_prints import (file_name,
                                             get_blueprints_routes_by_regex)
from logic.libs.rest.src.json import JSONEncoderCustom
from werkzeug.exceptions import HTTPException


def load_blueprints_by_path(app: Flask, blueprints_path: str):
    """
    Registra los archivos recursivamente dentro de del directorio como Blueprints para Flask,
    para esto es necesario que se defina un atributo llamado `blue_print` en cada archivo python. \n
    Ejemplo:

    ```
    from flask import Blueprint
    blue_print = Blueprint('nombre_unico_de_ruta', __name__, url_prefix='/api/v1/ejemplos')
    ```

    Es posible pasarle una regex. \n
    Ejemplo:

    ```
    'logic/apps/*/routes'
    ```
    """
    bps_paths = get_blueprints_routes_by_regex(blueprints_path)

    for bp_path in bps_paths:
        module_name = file_name(bp_path)

        spec = spec_from_file_location(module_name, bp_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)


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
