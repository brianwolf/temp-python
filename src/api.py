from flask import Flask
from logic.app.config.variables import setup_vars, Vars
# from logic.libs.logger import logger
from logic.libs.rest import rest
from logic.libs.variables.variables import get_var


setup_vars()

# directorio_logs = variables.get(variables_proyecto.Variable.DIRECTORIO_LOGS)
# nivel_logs = variables.dame(variables_proyecto.Variable.NIVEL_LOGS)
# logger.iniciar(directorio_logs, nivel_logs)

app = Flask(__name__)
rest.iniciar(app, 'logic/app/api')

print(get_var(Vars.PYTHON_HOST))

if __name__ == "__main__":
    flask_host = get_var(Vars.PYTHON_HOST)
    flask_port = 9000  # int(get_var(Vars.PYTHON_PORT))

    app.run(host=flask_host, port=flask_port, debug=True)
