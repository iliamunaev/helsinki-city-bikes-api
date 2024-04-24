import asyncpg

from src.postgres.repository import StationsRepository


class StationsService:
    def __init__(self, pool: asyncpg.Pool) -> None:
        self.stations_repo = StationsRepository(pool=pool)

    async def get_station_by_id(self, station_id: int):
        return await self.stations_repo.get_station_by_id(station_id=station_id)
