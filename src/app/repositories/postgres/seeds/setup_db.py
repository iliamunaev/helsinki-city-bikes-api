from postgres.database import async_engine
from src.app.api.stations import models
import asyncio


async def create_all_tables():
    try:
        async with async_engine.begin() as conn:
            print(models.Base.metadata.tables)
            print("Creating tables...")
            await conn.run_sync(models.Base.metadata.create_all)
            print("Tables created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(create_all_tables())
