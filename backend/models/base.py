from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from backend.config import Settings


class Base(DeclarativeBase):
    pass


'''
The Engine is a factory that can create new database connections for us, which also holds onto connections inside of a Connection Pool for fast reuse.
The echo=True parameter indicates that SQL emitted by connections will be logged to standard out.
'''

settings = Settings()
engine = create_engine(settings.DB_HOST, echo=True)


def create_tables():
	Base.metadata.create_all(engine)