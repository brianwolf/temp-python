from flask import Blueprint, jsonify, render_template
from logic.libs.logger.logger import logger
from logic.libs.variables.variables import all_vars

blue_print = Blueprint('api', __name__, url_prefix='',
                       template_folder='consume/static/web/', static_folder='consume/static/web/')


@blue_print.route('/vars')
def vars():
    return jsonify(all_vars())


@blue_print.route('/alive')
def alive():
    logger().info('ALIVE!')
    return jsonify({"state": "alive"})


# @blue_print.route('/')
# def index():
#     return render_template("index.html")
