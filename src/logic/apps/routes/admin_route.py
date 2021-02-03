from flask import jsonify
from flask_restplus import Resource
from logic.apps.config.rest import api
from logic.libs.logger.logger import logger
from logic.libs.variables.variables import all_vars

name_space = api.namespace('', description='Administracion de la aplicacion')


@name_space.route("/vars")
class Variables(Resource):

    def get(self):
        return jsonify(all_vars())


@name_space.route("/alive")
class Index(Resource):

    def get(self):
        logger().info('ALIVE!')
        return jsonify({"state": "alive"})
