from flask import Blueprint, jsonify, render_template
from flask_restplus import Resource
from logic.apps.config.rest import app, api
from logic.libs.logger.logger import logger
from logic.libs.variables.variables import all_vars

# blue_print = Blueprint(name='api', import_name=__name__, url_prefix='')


name_space = api.namespace('', description='Admin APIs')


@name_space.route("/vars")
class Variables(Resource):

    def get(self):
        return jsonify(all_vars())


@name_space.route("/alive")
class Index(Resource):

    def get(self):
        logger().info('ALIVE!')
        return jsonify({"state": "alive"})
