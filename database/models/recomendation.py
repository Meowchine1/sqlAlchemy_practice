 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base  import Base


class Recomendation(Base):
    __tablename__ = 'recomendations'
    
    id = Column(Integer, primary_key=True,  autoincrement=True)
    # Since we have a 1:n relationship, we need to store a foreign key 
    # to the users table.
    userId = Column(Integer, ForeignKey('users.id'))
    # Defines the 1:n relationship between users and recomendations.
    user = relationship("User", back_populates="recomendations")
    
    filmId = Column(Integer, ForeignKey('films.id'))
    film = relationship("Film", back_populates="recomendations")
    
    description = Column(String(256))
    date = Column(String, nullable=False)
    score = Column(Integer) #  TODO Оценка (0 - 10)
    def __repr__(self):
       return "description='%s'" % (
                               self.description)
