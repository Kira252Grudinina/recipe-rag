FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install uv && uv sync --no-dev

COPY src/ ./src/
COPY data/chroma ./data/chroma

CMD ["uv", "run", "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]