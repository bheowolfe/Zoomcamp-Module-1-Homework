FROM python:3.13.10-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" ./
COPY taxi_zone_lookup.csv /data/
COPY green_tripdata_2025-11.parquet /data/
RUN uv sync --locked

COPY lookup.py .

ENTRYPOINT ["python", "lookup.py"]