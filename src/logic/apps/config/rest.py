from flask import Flask
from flask_restplus import Api
from logic.libs.rest import rest

api = None
app = None

blueprints_path = 'logic/apps/*/routes'


def setup_rest(name: str) -> Flask:

    global app, blueprints_path, api

    app = Flask(name)
    app.config.setdefault('ERROR_INCLUDE_MESSAGE', False)

    api = Api(app)

    rest.load_generic_json_coders(api)
    rest.load_generic_error_handler(api)
    rest.load_blueprints_by_path(api, blueprints_path)

    return app
