FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev  # Exclude development dependencies.

COPY ./src .

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]

