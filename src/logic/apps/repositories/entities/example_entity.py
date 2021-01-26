from enum import Enum

from logic.apps.configs.variables import Variable
from logic.libs.variables.variables import dame


class TipoDB(Enum):
    SQLITE = 'SQLITE'
    MONGODB = 'MONGODB'


def tipo_db_usado() -> TipoDB:
    """
    Devuelve el tipo de la base de datos usado
    """
    return TipoDB[dame(Variable.DB_TIPO).upper()]
