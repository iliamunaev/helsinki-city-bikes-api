import pytest
from unittest.mock import AsyncMock

from src.app.repositories.postgres.repository import StationsRepository


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "station_id,expected_output",
    [
        (
            1,
            {
                "station_id": 1,
                "station_name": "Station One",
                "latitude": 34.05,
                "longitude": -118.25,
            },
        ),
        (
            2,
            {
                "station_id": 2,
                "station_name": "Station Two",
                "latitude": 40.71,
                "longitude": -74.01,
            },
        ),
        (999, None),  # Assuming station ID 999 does not exist
    ],
)
async def test_get_station_by_id(station_id, expected_output, mocker):
    mock_pool = AsyncMock()
    mock_fetchrow = AsyncMock()
    mock_pool.fetchrow = mock_fetchrow

    mock_fetchrow.return_value = expected_output

    repo = StationsRepository(pool=mock_pool)

    result = await repo.get_station_by_id(station_id)

    assert result == expected_output

    mock_fetchrow.assert_called_once_with(
        "SELECT * FROM stations WHERE station_id = $1", station_id
    )
