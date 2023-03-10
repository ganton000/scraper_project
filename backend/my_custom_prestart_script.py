from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from config import settings

Base = declarative_base()

## initialize env vars
username= settings.DB_USERNAME
password= settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
database_name = settings.DB_NAME

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)