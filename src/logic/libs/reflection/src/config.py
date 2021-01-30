from sqlalchemy.engine import Engine

URL_DEFAULT: str = ':memory:'
URL: str = URL_DEFAULT
ECHO: bool = False
ENTITIES_PATH: str = None

ENGINE: Engine = None
