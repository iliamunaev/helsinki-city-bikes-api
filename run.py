import uvicorn

from src.app.app import start_up_app
from src.app.settings import AppSettings

app_settings = AppSettings()

app = start_up_app(settings=app_settings)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=app_settings.PORT,
    )
