"""
Herramienta que carga de formma dinamica los blueprints de flask recursivamente
que se encuentren en un directorio
"""
import glob
import os
from importlib.util import module_from_spec, spec_from_file_location
from typing import List

from flask import Flask


def _file_name(path: str) -> str:
    """
    Devuelve el nombre del archivo al final de la ruta sin la extension
    """
    return os.path.basename(path).split('.')[0]


def _get_blueprints_routes(base_path: str) -> List[str]:
    """
    Obtiene las rutas de todos los archivos .py dentro del directorio parametro, 
    es recursivo por lo que si hay carpetas dentro tambien busca ahi
    """
    blueprints_routes = []

    for root, _, files in os.walk(base_path):

        if '__pycache__' in root or not files:
            continue

        blueprints_routes.extend([
            os.path.join(root, file)
            for file in files
        ])

    return blueprints_routes


def _get_blueprints_routes_by_regex(regex_path: str) -> List[str]:
    """
    Obtiene las rutas de todos los archivos python dentro del directorio parametro regex, 
    es recursivo por lo que si hay carpetas dentro tambien busca ahi
    """
    blueprints_routes = []

    for base_path in glob.glob(regex_path):
        blueprints_routes.extend(_get_blueprints_routes(base_path))

    return blueprints_routes


def load_blueprints(app: Flask, base_path: str):
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
    routes = _get_blueprints_routes_by_regex(base_path)

    for route in routes:
        nombre_modulo = _file_name(route)

        spec = spec_from_file_location(nombre_modulo, route)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, 'blue_print'):
            app.register_blueprint(module.blue_print)
