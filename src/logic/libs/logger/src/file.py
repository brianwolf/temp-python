import logging
import os

from logic.libs.logger.src import config


def make_logger(name: str = 'app', level: str = config.DEFAULT_LEVEL) -> logging.Logger:
    """
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea
    """
    if not os.path.exists(config.PATH):
        os.makedirs(config.PATH, exist_ok=True)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s (%(process)d) - %(levelname)s - %(message)s')

    sh = logging.StreamHandler()
    sh.setLevel(level)
    sh.setFormatter(formatter)

    ruta_log = os.path.join(config.PATH, f'{name}.log')
    fh = logging.FileHandler(ruta_log)
    fh.setLevel(level)
    fh.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger
