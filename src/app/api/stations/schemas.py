from pydantic import BaseModel, field_validator


# Pydantic models for the API


class Station(BaseModel):
    station_id: int
    station_name: str
    latitude: float
    longitude: float

    @field_validator("latitude")
    def check_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        return v

    @field_validator("longitude")
    def check_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return v


class StationName(BaseModel):
    station_name: str
