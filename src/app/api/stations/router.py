from typing import List

from fastapi import HTTPException, Depends, APIRouter
from .dependencies import get_stations_service
from .schemas import Station, StationName
from .servises import StationsService

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/names", response_model=List[StationName])
async def get_stations_names(
    get_stations_service: StationsService = Depends(get_stations_service),
) -> List[StationName]:
    stations_names = await get_stations_service.get_stations_names()
    return stations_names


@router.get("/{station_id}", response_model=Station)
async def get_station_by_id(
    station_id: int,
    get_stations_service: StationsService = Depends(get_stations_service),
) -> Station:

    station = await get_stations_service.get_station_by_id(station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station
