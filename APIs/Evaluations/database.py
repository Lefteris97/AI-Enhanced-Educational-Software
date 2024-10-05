from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#mysql+pymysql://username:password@localhost:port/database_name
URL_DATABASE = 'mysql+pymysql://admin:1234@localhost:3307/edusystem'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()