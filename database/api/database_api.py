
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy.sql import func
from sqlalchemy import select

from database.models.DbModel import Base, Film, User, Recomendation

import configparser

def getDbUrl():
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config.get('config', 'db.url')
    print(url)
    return url

def create_ifNotExist():
    url = getDbUrl()
    engine = create_engine(url)
    # Create all tables by issuing CREATE TABLE if not exist commands to the DB.
    Base.metadata.create_all(engine) 


def add(entity):
    engine = create_engine(getDbUrl())
    with Session(engine) as session:
        session.begin()
        try:
            session.add(entity)
        except:
            session.rollback()
            raise
        else:
            session.commit()

def delete(entity):
    engine = create_engine(getDbUrl())
    with Session(engine) as session:
        session.begin()
        try:
            session.delete(entity)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            

def update(entity):
    pass


def get_film_score(film):
    engine = create_engine(getDbUrl())
    with Session(engine) as session:
        
        session.begin()
        
        if type(film) == int:
            return session.query(func.avg(Recomendation.score))\
            .filter(Recomendation.filmId == film)\
                .scalar()
                
        elif type(film) == str:
            filmid = session.query(Film.id).filter(Film.name == film)
            return session.query(func.avg(Recomendation.score))\
            .filter(Recomendation.filmId == filmid)\
                .scalar()
        else:
            raise Exception("Incorrect input data: expected filmid or name") 
         
        
        
        
def get_film_by_name(film_name):
    pass
           

def get_user_byChatId(chatId):
    pass


def get_user_recomendations(chatId):
    pass


def get_film_recomendations(filmId):
    pass


      
def test_api():

    engine = create_engine(getDbUrl())
    Session = sessionmaker(bind=engine)
    session = Session()
    
    users = [
        User(username="Kate", date="somedate", rate=0, chatId="chatId1"),
        User(username="@Ivan", date="somedate", rate=0, chatId="chatId2"),
        User(username="@Olga", date="somedate", rate=0, chatId="chatId3"),
        User(username="@Ibragim", date="somedate", rate=0, chatId="chatId4")
        
    ]
    
    film = Film(name="Leon")
     
    
    recomendations = []
    for u, score in zip(users, range(len(users))):
        r = Recomendation(score=score)
        recomendations.append(r)
        u.recomendations = [r]
        film.recomendations += [r]
    
    session.add(film)
    for u, r in zip(users, recomendations):
        session.add(u)
        session.add(r)
    
    session.commit()

    # Now let's query the user that has the e-mail address ed@google.com
    # SQLAlchemy will construct a JOIN query automatically.
    # user_by_email = session.query(User)\
    #     .filter(Address.email_address=='ed@google.com')\
    #     .first()

    # print(user_by_email)

    # # This will cause an additional query by lazy loading from the DB.
    # print(user_by_email.addresses)


    # # To avoid querying again when getting all addresses of a user,
    # # we use the joinedload option. SQLAlchemy will load all results and hide
    # # the duplicate entries from us, so we can then get for
    # # the user's addressess without an additional query to the DB.
    # user_by_email = session.query(User)\
    #     .filter(Address.email_address=='ed@google.com')\
    #     .options(joinedload(User.addresses))\
    #     .first()

    # print(user_by_email)
    # print(user_by_email.addresses)
    

# -----------------------------------