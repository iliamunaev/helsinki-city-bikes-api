from sqlalchemy import Column, ForeignKey, Integer, String, Float
from postgres.db import Base
#  SQLAlchemy ORM Models


class Station(Base):
    __tablename__ = "stations"

    station_id = Column(Integer, primary_key=True)
    station_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


class Trip(Base):
    __tablename__ = "trips"

    trip_id = Column(Integer, primary_key=True)
    departure_station_id = Column(Integer, ForeignKey("stations.station_id"))
    return_station_id = Column(Integer, ForeignKey("stations.station_id"))
    departure_year = Column(Integer)
    departure_month = Column(Integer)
    departure_day = Column(Integer)
    departure_hour = Column(Integer)
    departure_min = Column(Integer)
    return_year = Column(Integer)
    return_month = Column(Integer)
    return_day = Column(Integer)
    return_hour = Column(Integer)
    return_min = Column(Integer)
    distance_m = Column(Integer)
    duration_min = Column(Integer)
    speed_avg_km_h = Column(Float)
    air_temperature_deg_c = Column(Float)
