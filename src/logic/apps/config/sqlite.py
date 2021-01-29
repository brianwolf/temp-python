import os
from pathlib import Path

from logic.apps.config.variables import Vars, get_var
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = None


def setup_sqlite():

    global engine

    db_path = get_var(Vars.DB_SQLITE_PATH)

    Path(os.path.dirname(db_path)).mkdir(parents=True, exist_ok=True)

    url_db = f'sqlite:///{db_path}'

    engine = create_engine(url_db, echo=True)

    _load_migrations()


def create_session() -> Session:
    return sessionmaker(engine)


# TODO: hacer una util para cargar modulos como en REST
def _load_migrations():
    import logic.apps.repositories.entities.example_entity
