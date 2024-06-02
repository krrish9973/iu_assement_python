from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# SQL Lite DB URL
DB_URL = "sqlite:///./sql_app.db"
Base = declarative_base()
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()