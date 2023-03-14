import mysql.connector

from config import settings
from models.base import Base


## initialize env vars
username= settings.DB_USERNAME
password= settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
database_name = settings.DB_NAME

SQL_DATABASE_PARAMS = {
	"host": host,
	"user": username,
	"password": password,
	"database": database_name,
	"port": port
}


def create_tables():
	pass


def get_db() -> Session:
	db = Session()
	try:
		yield db
	finally:
		db.close()
