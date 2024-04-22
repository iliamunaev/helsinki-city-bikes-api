import pytest
from pydantic import ValidationError

from src.postgres.models import Station


@pytest.mark.parametrize(
    "latitude, expected_result",
    [
        (-90, True),
        (0, True),
        (90, True),
        (-91, ValueError),
        (91, ValueError)
    ]
)
def test_latitude_validation(latitude, expected_result):
    if expected_result:
        station = Station(station_id=1, station_name="Central", latitude=latitude, longitude=0.0)
        assert station.latitude == latitude
    else:
        with pytest.raises(ValidationError):
            Station(station_id=1, station_name="Central", latitude=latitude, longitude=0.0)


@pytest.mark.parametrize(
    "longitude, expected_result",
    [
        (-180, True),
        (0, True),
        (180, True),
        (-181, ValueError),
        (181, ValueError)
    ]
)
def test_longitude_validation(longitude, expected_result):
    if expected_result:
        station = Station(station_id=1, station_name="Central", latitude=0.0, longitude=longitude)
        assert station.longitude == longitude
    else:
        with pytest.raises(ValidationError):
            Station(station_id=1, station_name="Central", latitude=0.0, longitude=longitude)
