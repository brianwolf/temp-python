from typing import List

from logic.apps.models.example import Example
from logic.apps.repositories.entities.example_entity import ExampleEntity
from logic.libs.sqliteAlchemy import sqliteAlchemy


def get_all() -> List[Example]:

    s = sqliteAlchemy.make_session()
    result = s.query(ExampleEntity).all()
    s.close()

    return [r.to_model() for r in result]


def add(m: Example) -> int:

    s = sqliteAlchemy.make_session()

    e = ExampleEntity.from_model(m)
    s.add(e)

    s.commit()
    s.flush()

    return e.id
