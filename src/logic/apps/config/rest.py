from flask import Flask
from flask_restplus import Api, Resource
from logic.libs.rest import rest

_app = None
_blueprints_path = 'logic/apps/*/routes'


def setup_rest(name: str) -> Flask:

    global _app, _blueprints_path

    _app = Flask(name)
    rest.setup(_app, _blueprints_path)

    swagger = Api(app=_app)
    name_space = swagger.namespace('main', description='Main APIs')

    @name_space.route("/docs")
    class MainClass(Resource):
        def get(self):
            return {
                "status": "Got new data"
            }

        def post(self):
            return {
                "status": "Posted new data"
            }

    return _app
