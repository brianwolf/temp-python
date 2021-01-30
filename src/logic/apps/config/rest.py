from flask import Flask
from flask_restplus import Api
from logic.libs.reflection import reflection
from logic.libs.rest import rest

api = None
app = None

_blueprints_path = 'logic/apps/routes'


def setup_rest(name: str) -> Flask:

    global app, api

    app = Flask(name)
    app.config.setdefault('ERROR_INCLUDE_MESSAGE', False)

    api = Api(app)

    rest.load_generic_json_coders(api)
    rest.load_generic_error_handler(api)

    reflection.load_modules_by_path(_blueprints_path)

    return app
