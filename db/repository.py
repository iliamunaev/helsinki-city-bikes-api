import asyncpg


class StationsRepository:
    def __init__(self, pool: asyncpg.Pool) -> None:
        self.pool = pool

    async def get_station_by_id(self, station_id: int) -> dict | None:
        record = await self.pool.fetchrow(
            "SELECT * FROM stations WHERE station_id = $1", station_id
        )
        return dict(record) if record else None

    async def get_stations_names(self):
        records = await self.pool.fetch("SELECT station_name FROM stations")
        return [dict(record) for record in records]
