from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models.Base import Base
from models.film import Film
from models.user import User
from models.recomendation import Recomendation
from api.database_api import getDbUrl


# config = configparser.ConfigParser()
# config.read('alembic.ini')
url = getDbUrl()
engine = create_engine(url)
# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine) 
 