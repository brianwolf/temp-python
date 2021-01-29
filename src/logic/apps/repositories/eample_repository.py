from typing import List

from logic.apps.config.sqlite import create_session
from logic.apps.models.example import Example
from logic.apps.repositories.entities.example_entity import ExampleEntity


def get_all() -> List[Example]:

    s = create_session()
    result = s.query(ExampleEntity).all()
    s.close()

    return [r.to_model() for r in result]
