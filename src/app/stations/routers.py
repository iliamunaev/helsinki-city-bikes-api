from fastapi import HTTPException, Depends, APIRouter

from src.schemas import Station
from src.app.stations.servises import StationsService
from src.depends import get_stations_service

router = APIRouter()


@router.get("/")
def index():
    return {"Hello": "World"}


@router.get("/stations/{station_id}", response_model=Station)
async def get_station_by_id(station_id: int,
                            get_stations_service: StationsService = Depends(get_stations_service),
                            ) -> Station:
    station = await get_stations_service.get_station_by_id(station_id=station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station
