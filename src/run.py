import uvicorn

from app.settings import AppSettings
from main import start_up_app

app_settings = AppSettings()

app = start_up_app(settings=app_settings)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=app_settings.PORT,
    )
