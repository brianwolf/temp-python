from flask import Flask

from logic.app.config.logger import setup_loggers
from logic.app.config.variables import Vars, setup_vars
from logic.libs.rest import rest
from logic.libs.variables.variables import get_var

setup_vars()
setup_loggers()


app = Flask(__name__)
rest.setup(app, 'logic/app/api')


if __name__ == "__main__":
    flask_host = get_var(Vars.PYTHON_HOST)
    flask_port = int(get_var(Vars.PYTHON_PORT))

    app.run(host=flask_host, port=flask_port, debug=True)
