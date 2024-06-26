import asyncpg
from fastapi import FastAPI

from app.settings import PostgresSettings, AppSettings
from app.api.stations.router import router as stations_router


async def setup_pg_pool(app: FastAPI) -> None:
    pg_settings = PostgresSettings()
    pool = await asyncpg.create_pool(dsn=pg_settings.url)
    app.state.pool = pool


def start_up_app(settings: AppSettings) -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
    )

    @app.on_event("startup")
    async def startup() -> None:
        await setup_pg_pool(app)

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await app.state.pool.close()

    app.include_router(stations_router, prefix="/stations")

    return app
