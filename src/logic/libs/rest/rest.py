"""
Rest
----

Configura el app de Flask para cargar blueprints dinamicamente, agregar JSON decoders que sigan un estandar, 
agregar handlers para manejo automatico de errores, entre otros.
"""
from flask import Flask

from logic.libs.rest.src.blue_prints import load_blueprints
from logic.libs.rest.src.error_handlers import error_handler_bp
from logic.libs.rest.src.json import JSONEncoderCustom


def setup(app: Flask, routes_path: str):
    """
    Configura flask cargandole los blueprints dentro de la ruta parametro y handlers de errores.
    Es posible enviarle un regex como ruta tal que asi:

    ```
    'logic/apps/*/routes'
    ```
    """
    app.register_blueprint(error_handler_bp)
    app.json_encoder = JSONEncoderCustom

    load_blueprints(app, routes_path)
