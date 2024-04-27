import pytest
from pydantic import ValidationError

from src.app.api.stations.schemas import Station


@pytest.mark.parametrize(
    "latitude, expected_result",
    [
        (-90.0, -90.0),
        (0.0, 0.0),
        (90.0, 90.0),
        (-91.0, ValueError),
        (91.0, ValueError)
    ]
)
def test_latitude_validation(latitude, expected_result):
    if isinstance(expected_result, float):
        station = Station(station_id=1, station_name="Central", latitude=latitude, longitude=0.0)
        assert station.latitude == latitude
    else:
        with pytest.raises(ValidationError):
            Station(station_id=1, station_name="Central", latitude=latitude, longitude=0.0)

@pytest.mark.parametrize(
    "longitude, expected_result",
    [
        (-180.0, -180.0),
        (0.0, 0.0),
        (180.0, 180.0),
        (-181.0, ValueError),
        (181.0, ValueError)
    ]
)
def test_longitude_validation(longitude, expected_result):
    if isinstance(expected_result, float):
        station = Station(station_id=1, station_name="Central", latitude=0.0, longitude=longitude)
        assert station.longitude == longitude
    else:
        with pytest.raises(ValidationError):
            Station(station_id=1, station_name="Central", latitude=0.0, longitude=longitude)
