from enum import Enum

from logic.libs.variables.variables import Config, get_var, setup


class Vars(Enum):
    VERSION = 'VERSION'
    PYTHON_HOST = 'PYTHON_HOST'
    PYTHON_PORT = 'PYTHON_PORT'
    LOGS_LEVEL = 'LOGS_LEVEL'
    LOGS_PATH = 'LOGS_PATH'
    TEMP_PATH = 'TEMP_PATH'
    DB_SQLITE_PATH = 'DB_SQLITE_PATH'


def setup_vars():
    setup([
        Config(
            file_path='consume/config/variables.env',
            hiden_vars=['LOGS_LEVEL'],
            enum_vars=Vars)
    ])
