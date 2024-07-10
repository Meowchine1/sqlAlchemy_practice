from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

 
engine = create_engine("sqlite:///kinoBot.db")

# The base class which our objects will be defined on.
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    username = Column(String(20), nullable=False)
    date = Column(String(20), nullable=False)
    recomendationCount = Column(Integer, nullable=False)
    rate = Column(Integer, nullable=False)
    
    recomendations = relationship("Recomendation", back_populates="user")
    
    def __repr__(self):
       return "Username='%s', date='%s'" % (
                               self.username, self.date)

 
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


class Recomendation(Base):
    __tablename__ = 'recomendations'
    
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


# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine) 

# Creates a new session to the database by using the engine we described.
Session = sessionmaker(bind=engine)
session = Session()

# Let's create a user and add two e-mail addresses to that user.
ed_user = User(username="@someuser", date="somedate", recomendationCount=0, rate=0)
ed_film = Film(name="somefilm")

ed_rec = Recomendation(userId=ed_user.id, filmId=ed_film.id)
ed_user.recomendations = [ed_rec]
ed_film.recomendations = [ed_rec]

 
# Let's add the user and its addresses we've created to the DB and commit.
session.add(ed_user)
session.add(ed_film)
session.add(ed_rec)
session.commit()

# Now let's query the user that has the e-mail address ed@google.com
# SQLAlchemy will construct a JOIN query automatically.
user_by_email = session.query(User)\
    .filter(Address.email_address=='ed@google.com')\
    .first()

print user_by_email

# This will cause an additional query by lazy loading from the DB.
print user_by_email.addresses


# To avoid querying again when getting all addresses of a user,
# we use the joinedload option. SQLAlchemy will load all results and hide
# the duplicate entries from us, so we can then get for
# the user's addressess without an additional query to the DB.
user_by_email = session.query(User)\
    .filter(Address.email_address=='ed@google.com')\
    .options(joinedload(User.addresses))\
    .first()

print user_by_email
print user_by_email.addresses