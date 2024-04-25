from sqlalchemy import Column, ForeignKey, SmallInteger, String, Float
from sqlalchemy.orm import declarative_base

#  SQLAlchemy ORM Models

Base = declarative_base()


class Station(Base):
    __tablename__ = "stations"

    station_id = Column(SmallInteger, primary_key=True, nullable=False)
    station_name = Column(String(50), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
