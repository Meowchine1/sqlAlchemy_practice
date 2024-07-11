
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from database.models.film import Film
from database.models.user import User
from database.models.recomendation import Recomendation
import configparser


def getDbUrl():
    config = configparser.ConfigParser()
    config.read('alembic.ini')
    url = config.get('alembic', 'sqlalchemy.url')
    print(url)
    return url


 

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
            session.add(entity)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            

def update(entity):
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
            
          
def test_api():
    engine = create_engine(getDbUrl())
    # Creates a new session to the database by using the engine we described.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Let's create a user and add two e-mail addresses to that user.
    ed_user = User(username="@someuser", date="somedate", recomendationCount=0, rate=0)
    ed_film = Film(name="somefilm")

    ed_rec = Recomendation(userId=ed_user.id, filmId=ed_film.id, date="some")
    ed_user.recomendations = [ed_rec]
    ed_film.recomendations = [ed_rec]

    
    # Let's add the user and its addresses we've created to the DB and commit.
    session.add(ed_user)
    session.add(ed_film)
    session.add(ed_rec)
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