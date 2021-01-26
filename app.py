from logic.apps.config.logger import setup_loggers
from logic.apps.config.rest import setup_rest
from logic.apps.config.variables import Vars, setup_vars
from logic.libs.variables.variables import get_var

setup_vars()
setup_loggers()
app = setup_rest(__name__)


if __name__ == "__main__":
    flask_host = get_var(Vars.PYTHON_HOST)
    flask_port = int(get_var(Vars.PYTHON_PORT))

    app.run(host=flask_host, port=flask_port, debug=False)
