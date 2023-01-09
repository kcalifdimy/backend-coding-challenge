import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#This line of code is used to get the project root directory
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


#This line of code is used to get the path to the futures folder where all the json
# json file are stored 
FIXTURE_DIR_PATH = (os.path.join(ROOT_DIR, "backend-coding-challenge/", "fixtures"))
FILE_TEST_DIR_PATH = (os.path.join(ROOT_DIR, "backend-coding-challenge/", "files"))


#The database path
DB_FILE_PATH = (os.path.join(ROOT_DIR, "backend-coding-challenge/", "planning.db"))


# This function creates the database file if it's empty
def create_db_file():
    if not os.path.isfile(DB_FILE_PATH):
     file=open(DB_FILE_PATH, 'w+')


#The codes below are used to conneect to the database and create database table
SQLALCHAMY_DATABASE_URL = 'sqlite:///./planning.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() 
    try:
        yield db 
    finally:  
        db.close()

