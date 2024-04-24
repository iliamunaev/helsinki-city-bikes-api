import pytest
from unittest.mock import AsyncMock

from src.postgres.repository import StationsRepository


@pytest.mark.asyncio
async def test_get_stations_names():
    mock_pool = AsyncMock()
    mock_fetch = AsyncMock()
    mock_pool.fetch = mock_fetch

    expected_records = [{"station_name": "Station One"}, {"station_name": "Station Two"}]
    mock_fetch.return_value = expected_records

    # Initialize the repository with the mock pool
    repo = StationsRepository(pool=mock_pool)

    # Call the method under test
    result = await repo.get_stations_names()

    # Assert that the fetch method was called with the correct query
    mock_fetch.assert_called_once_with("SELECT station_name FROM stations")

    # Assert that the result matches the expected format
    expected_output = [{"station_name": "Station One"}, {"station_name": "Station Two"}]
    assert result == expected_output
