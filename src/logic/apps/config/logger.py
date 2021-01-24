from logic.apps.config.variables import Vars
from logic.libs.logger.logger import setup
from logic.libs.variables.variables import get_var


def setup_loggers():
    setup(get_var(Vars.DIRECTORIO_LOGS), get_var(Vars.NIVEL_LOGS))
