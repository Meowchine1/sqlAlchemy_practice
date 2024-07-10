 
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from films import Films
from users import Users

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Recomendations(Base):
    __tablename__ = 'Recomendations'
    UserId = Column(Integer, ForeignKey('Users.Id'))
    FilmId = Column(Integer, ForeignKey('Films.Id'))
    Date = Column(String, nullable=False)
    Score = Column(Integer) #  Оценка (0 - 10)
