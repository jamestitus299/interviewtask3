from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create an engine instance
engine = create_engine('sqlite:///vchat.db')

# Create a declarative base
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

# Define a Question Answer
class QA(Base):
    __tablename__ = 'qa'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    user = Column(String)
    answer = Column(String)
    

# Create the database tables
def create_db():
    """Create the databse with the tables."""
    Base.metadata.create_all(engine)