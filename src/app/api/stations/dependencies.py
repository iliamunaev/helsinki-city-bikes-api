from fastapi import Request
from .servises import StationsService


async def get_stations_service(request: Request) -> StationsService:
    return StationsService(pool=request.app.state.pool)
