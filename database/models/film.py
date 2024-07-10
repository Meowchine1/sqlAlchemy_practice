 
 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class Film(Base):
    __tablename__ = 'films'
    
    id = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String(50), nullable=False)
    href = Column(String)
    description = Column(String(256))
    img = Column(String)
    recomendations = relationship("Recomendation", back_populates="film")
    def __repr__(self):
       return "name='%s'" % (
                               self.name)
    
    