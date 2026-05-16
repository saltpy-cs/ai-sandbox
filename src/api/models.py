from sqlalchemy import Boolean, Column, Float, Integer, String
from database import Base


class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Float, nullable=True)
    sex = Column(String, nullable=False)
    pclass = Column(Integer, nullable=False)
    survived = Column(Boolean, nullable=False)
