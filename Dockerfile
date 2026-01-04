# ---------- base ----------
FROM python:3.11-slim

# ---------- env ----------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------- system deps ----------
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ---------- workdir ----------
WORKDIR /app

# ---------- python deps ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- app code ----------
COPY src ./src
COPY migration ./migration
COPY alembic.ini .

# ---------- runtime ----------
CMD ["python", "-m", "src.main"]
