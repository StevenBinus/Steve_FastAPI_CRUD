# import library module
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# database connection
load_dotenv()
user = os.getenv('user') 
password = os.getenv('password')
host = os.getenv('host')
db_name = os.getenv('db_name')
database_url = f'mssql+pymssql://{user}:{password}@{host}/{db_name}'

# basic infrastructure to use ORM library
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# function to get a database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
