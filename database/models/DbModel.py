from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Base(DeclarativeBase): pass

class Film(Base):
    __tablename__ = 'films'
    
    id = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String(50), nullable=False)
    href = Column(String)
    description = Column(String(256))
    img = Column(String)
    recomendations = relationship("Recomendation", back_populates="film")
    
    def __repr__(self):
       return "name='%s'" % (self.name)
       
       
class Recomendation(Base):
    __tablename__ = 'recomendations'
    
    id = Column(Integer, primary_key=True,  autoincrement=True)
    
    chatId = Column(Integer, ForeignKey('users.chatId'))
    user = relationship("User", back_populates="recomendations")
    filmId = Column(Integer, ForeignKey('films.id'))
    film = relationship("Film", back_populates="recomendations")
    
    description = Column(String(256))
    score = Column(Integer) #  TODO Оценка (0 - 10)
    
    def __repr__(self):
       return "description='%s'" % (self.description)
       
class User(Base):
    __tablename__ = 'users'
    
    chatId = Column(String(250), nullable=False,  primary_key=True)
    username = Column(String(20), nullable=False)
    date = Column(String(20), nullable=False)
    rate = Column(Integer, nullable=False)
    recomendations = relationship("Recomendation", back_populates="user")
    
    def __repr__(self):
       return "Username='%s', date='%s'" % (self.username, self.date)