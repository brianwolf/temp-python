from flask import Blueprint, jsonify, render_template
from logic.libs.logger.logger import logger
from logic.libs.variables.variables import all_vars

blue_print = Blueprint('api', __name__, url_prefix='')


@blue_print.route('/vars')
def vars():
    return jsonify(all_vars())


@blue_print.route('/alive')
def alive():
    logger().info('ALIVE!')
    return jsonify({"state": "alive"})
