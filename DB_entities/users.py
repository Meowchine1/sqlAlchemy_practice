from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Users(Base):
    __tablename__ = 'Users'
    Id = Column(Integer, primary_key=True,  autoincrement=True)
    Username = Column(String, nullable=False)
    Date = Column(String, nullable=False)
    RecomendationCount = Column(Integer)
    Rate = Column(Integer)


 