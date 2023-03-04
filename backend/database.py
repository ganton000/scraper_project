from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Settings
from models.base import create_engine, Base


settings = Settings()

## initialize env vars
username= settings.DB_USERNAME
password= settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
database_name = settings.DB_NAME

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'


'''
The Engine is a factory that can create new database connections for us, which also holds onto connections inside of a Connection Pool for fast reuse.
The echo=True parameter indicates that SQL emitted by connections will be logged to standard out.
'''

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
	Base.metadata.create_all(engine)


def get_db() -> Session:
	db = Session()
	try:
		yield db
	finally:
		db.close()
