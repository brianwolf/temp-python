"""
SQLiteAlchemy
---------
1.0.0

Utiliza sqlAlchemy para establecer una uncia conexion con un sqlite local, es para uso simple sin tanta configuracion
"""
from logic.libs.sqliteAlchemy.src import config
from logic.libs.sqliteAlchemy.src.sqlAlchemyMethods import create_engine
from sqlalchemy.orm import Session, sessionmaker


def setup(url: str, echo: bool = False, entities_path: str = None):
    """
    Configura la util, se debe usar antes de usar cualquier otro metodo

    - url -> es para la conexion, se lo pasa al metodo create_engine() de sqlAlchemy
    - echo -> si esta en True loguea todo los comandos ejecutados en sqlite con INFO
    """
    config.URL = url
    config.ECHO = echo
    config.ENTITIES_PATH = entities_path


def make_session() -> Session:
    """
    Crea una nueva session para conectarse a la BD
    """
    if not config.ENGINE:
        create_engine()

    return sessionmaker(config.ENGINE)
