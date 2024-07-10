 
 
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Films(Base):
    __tablename__ = 'Films'
    Id = Column(Integer, primary_key=True,  autoincrement=True)
    Name = Column(String)
    
    