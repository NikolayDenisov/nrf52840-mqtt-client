import os

from sqlalchemy import URL


def get_env(name: str, default=None, required: bool = False):
    value = os.getenv(name, default)
    if required and value is None:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


# MQTT
MQTT_BROKER = get_env("MQTT_BROKER", required=True)
MQTT_PORT = int(get_env("MQTT_PORT", 1883))
MQTT_TOPIC = get_env("MQTT_TOPIC", "sensors/#")

# Postgres
DATABASE_URL = URL.create(
    "postgresql+asyncpg",
    username=get_env("POSTGRES_USERNAME", required=True),
    password=get_env("POSTGRES_PASSWORD", required=True),
    host=get_env("POSTGRES_HOST", required=True),
    port=int(get_env("POSTGRES_PORT", 5432)),
    database=get_env("POSTGRES_DB", required=True),
)
