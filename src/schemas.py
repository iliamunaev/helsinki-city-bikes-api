from pydantic import BaseModel, field_validator


# Pydantic models for the API


class Station(BaseModel):
    station_id: int
    station_name: str
    latitude: float
    longitude: float

    @field_validator('latitude')
    def check_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        return v

    @field_validator('longitude')
    def check_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return v


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

