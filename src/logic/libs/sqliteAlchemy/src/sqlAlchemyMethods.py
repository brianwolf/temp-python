import os
from pathlib import Path

import sqlalchemy
from logic.libs.sqliteAlchemy.src import config
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


def create_engine():
    """
    Crea un engine usando el metodo create_engine() de sqlAlchemy
    """
    _create_subdirectories(config.URL)

    final_url = f'sqlite:///{config.URL}'

    config.ENGINE = sqlalchemy.create_engine(final_url, echo=config.ECHO)


def _create_subdirectories(path_file: str):
    """
    Crea los subdirectorios en caso de que no existan
    """

    if path_file == config.URL_DEFAULT:
        return

    Path(os.path.dirname(path_file)).mkdir(parents=True, exist_ok=True)
