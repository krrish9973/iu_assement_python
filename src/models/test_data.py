from sqlalchemy import Column, Float, Integer
from iu_assement_python.src.database import engine, Base
class TestData(Base):
    __tablename__ = 'test_data'
    id =  Column(Integer, primary_key=True,autoincrement=True)
    x = Column(Float)
    y = Column(Float)
    ideal_function_id = Column(Integer)
    deviation = Column(Float)

Base.metadata.create_all(engine)
