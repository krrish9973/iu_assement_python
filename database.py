from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

#SQL Lite DB URL
DB_URL =  "sqlite:///./sql_app.db"
engine = create_engine(DB_URL,connect_args={"check_same_thread":False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()