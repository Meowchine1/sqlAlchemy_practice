from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base  import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True,  autoincrement=True)
    username = Column(String(20), nullable=False)
    date = Column(String(20), nullable=False)
    #age = Column(Integer)
    recomendationCount = Column(Integer, nullable=False)
    rate = Column(Integer, nullable=False)
    recomendations = relationship("Recomendation", back_populates="user")
    
    def __repr__(self):
       return "Username='%s', date='%s'" % (
                               self.username, self.date)


 