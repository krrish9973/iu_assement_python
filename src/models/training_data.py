from sqlalchemy import Column, Float, Integer
#from iu_assement_python.src.database import Base, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DB_URL = "sqlite:///./sql_app.db"
Base = declarative_base()
engine = create_engine(DB_URL,connect_args={"check_same_thread":False})

class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True,autoincrement=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

Base.metadata.create_all(engine)