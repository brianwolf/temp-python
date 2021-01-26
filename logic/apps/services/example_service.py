
from logic.apps.models.example import Example
from datetime import datetime
from uuid import uuid4


def get_example() -> Example:
    """
    Devuelve un objeto de ejemplo
    """
    return Example(
        string='string',
        integer=2,
        date_time=datetime.now(),
        double=2.3,
        uuid=uuid4())
