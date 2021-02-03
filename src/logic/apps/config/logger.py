from logic.apps.config.variables import Vars
from logic.libs.logger.logger import setup
from logic.libs.variables.variables import get_var


def setup_loggers():
    setup(
        path=get_var(Vars.LOGS_PATH),
        level=get_var(Vars.LOGS_LEVEL)
    )
