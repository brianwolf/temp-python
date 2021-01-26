"""
Logger
-------
1.0.0

Crea logs de la aplicacion
"""
import logging

from logic.libs.logger.src import config
from logic.libs.logger.src.file import make_logger


def setup(path: str, default_level: str):
    """
    Configura el logger para el proyecto
    """
    config.PATH = path
    config.DEFAULT_LEVEL = default_level


def logger(nombre: str = 'app') -> logging.Logger:
    """
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea
    """
    if nombre not in config.LOGGERS:
        config.LOGGERS[nombre] = make_logger(nombre)

    return config.LOGGERS[nombre]
