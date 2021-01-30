from uuid import uuid4

from logic.apps.models.example import Example
from logic.libs.sqliteAlchemy import sqliteAlchemy
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExampleEntity(Base):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True, autoincrement=True)
    string = Column(String)
    integer = Column(Integer)
    date_time = Column(DateTime)
    double = Column(Float)
    uuid = Column(String)

    def to_model(self) -> Example:
        return Example(
            id=self.id,
            string=self.string,
            integer=self.integer,
            date_time=self.date_time,
            double=self.double,
            uuid=uuid4(self.uuid)
        )


Base.metadata.create_all(sqliteAlchemy.get_engine())
