from flask import Flask
from logic.libs.rest import rest

_app = None
_blueprints_path = 'logic/apps/*/routes'


def setup_rest(name: str) -> Flask:

    global _app, _blueprints_path

    _app = Flask(name)
    rest.setup(_app, _blueprints_path)

    return _app
