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


class Trip(Base):
    __tablename__ = "trips"

    trip_id = Column(SmallInteger, primary_key=True, nullable=False)
    departure_station_id = Column(SmallInteger, ForeignKey("stations.station_id"), nullable=False)
    return_station_id = Column(SmallInteger, ForeignKey("stations.station_id"), nullable=False)
    departure_year = Column(SmallInteger)
    departure_month = Column(String(9))
    departure_day = Column(SmallInteger)
    departure_hour = Column(SmallInteger)
    departure_min = Column(SmallInteger)
    return_year = Column(SmallInteger)
    return_month = Column(String(9))
    return_day = Column(SmallInteger)
    return_hour = Column(SmallInteger)
    return_min = Column(SmallInteger)
    distance_m = Column(SmallInteger)
    duration_min = Column(SmallInteger)
    speed_avg_km_h = Column(Float)
    air_temperature_deg_c = Column(Float)
