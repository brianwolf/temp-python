import logging
import os
from logging.handlers import TimedRotatingFileHandler

from logic.libs.logger.src import config


def make_logger(name: str, fh: logging.Handler) -> logging.Logger:
    """
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea
    """
    sh = logging.StreamHandler()
    sh.setLevel(config.DEFAULT_LEVEL)
    sh.setFormatter(config.DEFAULT_FORMATER)

    if not fh:
        fh = build_default_file_handler()

    logger = logging.getLogger(name)
    logger.setLevel(config.DEFAULT_LEVEL)
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger


def build_default_file_handler() -> logging.Handler:
    """
    Configura el fileHandler predefinido
    """

    if not os.path.exists(config.DEFAULT_PATH):
        os.makedirs(config.DEFAULT_PATH, exist_ok=True)

    fh = TimedRotatingFileHandler(
        os.path.join(config.DEFAULT_PATH, f'{config.DEFAULT_FILE_NAME}.log'),
        when="d",
        interval=1,
        backupCount=7)

    fh.setLevel(config.DEFAULT_LEVEL)
    fh.setFormatter(config.DEFAULT_FORMATER)

    return fh
