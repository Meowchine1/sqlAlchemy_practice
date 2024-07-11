from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from database.models.Base import Base
from database.models.film import Film
from database.models.user import User
from database.models.recomendation import Recomendation
from database.api.database_api import getDbUrl


def create_db():
    # config = configparser.ConfigParser()
    # config.read('alembic.ini')
    url = getDbUrl()
    engine = create_engine(url)
    # Create all tables by issuing CREATE TABLE commands to the DB.
    Base.metadata.create_all(engine) 
 