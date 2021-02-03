"""
Logger
-------
1.0.0

Crea logs de la aplicacion
"""
import logging

from logic.libs.logger.src import config
from logic.libs.logger.src.file import build_default_file_handler, make_logger


def setup(
        path: str = config.DEFAULT_PATH,
        level: str = config.DEFAULT_LEVEL,
        formater: str = config.DEFAULT_FORMATER,
        file_name: str = config.DEFAULT_FILE_NAME,
        handler: logging.Handler = None):
    """
    Configura las opciones PREDEFINIDAS del logger para el proyecto, en caso del handler, 
    el que viene rota los logs con un archivo por dia hasta hasta un maximo de 7 archivos.
    """
    config.DEFAULT_PATH = path
    config.DEFAULT_LEVEL = level
    config.DEFAULT_FORMATER = formater
    config.DEFAULT_FILE_NAME = file_name
    config.DEFAULT_HANDLER = handler if handler else build_default_file_handler()


def logger(
    name: str = config.DEFAULT_FILE_NAME,
    handler: logging.Handler = None
) -> logging.Logger:
    """
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea.\n
    En caso de pasarle un fileHandler el path del mismo debe existir 
    """
    if name not in config.LOGGERS:
        config.LOGGERS[name] = make_logger(name, handler)

    return config.LOGGERS[name]
