# import library module
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database connection
user = 'steve'
password = 'Internship2023'
host = '10.1.32.64'
db_name = 'DMSLIVE'
database_url = f"mssql+pymssql://{user}:{password}@{host}/{db_name}"

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
