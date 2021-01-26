from enum import Enum

from logic.libs.variables.variables import setup, Config


class Vars(Enum):
    VERSION = 'VERSION'
    PYTHON_HOST = 'PYTHON_HOST'
    PYTHON_PORT = 'PYTHON_PORT'
    NIVEL_LOGS = 'NIVEL_LOGS'
    DIRECTORIO_LOGS = 'DIRECTORIO_LOGS'
    DIRECTORIO_SISTEMA_ARCHIVOS = 'DIRECTORIO_SISTEMA_ARCHIVOS'
    DIRECTORIO_TEMP = 'DIRECTORIO_TEMP'
    DB_SQLITE_SCRIPT = 'DB_SQLITE_SCRIPT'
    DB_SQLITE_RUTA = 'DB_SQLITE_RUTA'
    DB_TIPO = 'DB_TIPO'


def setup_vars():
    setup([
        Config(
            file_path='consume/config/variables.env',
            hiden_vars=['NIVEL_LOGS'],
            enum_vars=Vars)
    ])
