from pydantic import BaseModel


# Pydantic models for the API


class Trip(BaseModel):
    trip_id: int
    departure_station_id: int
    return_station_id: int
    departure_year: int
    departure_month: str
    departure_day: int
    departure_hour: int
    departure_min: int
    return_year: int
    return_month: str
    return_day: int
    return_hour: int
    return_min: int
    distance_m: int
    duration_min: int
    speed_avg_km_h: int
    air_temperature_deg_c: int


class StationName(BaseModel):
    station_name: str