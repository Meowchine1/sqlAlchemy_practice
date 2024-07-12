from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base  import Base

class User(Base):
    __tablename__ = 'users'
    
    chatId = Column(String(250), nullable=False,  primary_key=True)
    username = Column(String(20), nullable=False)
    date = Column(String(20), nullable=False)
    rate = Column(Integer, nullable=False)
    recomendations = relationship("Recomendation", back_populates="user")
    
    def __repr__(self):
       return "Username='%s', date='%s'" % (
                               self.username, self.date)


 