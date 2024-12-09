from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine('sqlite:///mydatabase.db')

# Create a SessionMaker instance
SessionMaker = sessionmaker(bind=engine)

# Create a session
session = SessionMaker()