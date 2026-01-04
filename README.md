# MQTT → PostgreSQL Service

Сервис для асинхронного приёма данных от MQTT-брокера и сохранения их в
PostgreSQL.

Используется для сохранения данных от IoT-устройств (например, nRF52840 с
датчиками температуры/влажности).

---

## 📌 Возможности

* Подписка на MQTT-топики
* Асинхронная обработка сообщений
* Сохранение данных в PostgreSQL
* SQLAlchemy 2.x (async)
* Alembic для миграций
* Конфигурация через переменные окружения

---

## 🧱 Архитектура

```
MQTT Broker
    |
    v
paho-mqtt (thread)
    |
    v
asyncio.Queue
    |
    v
Async SQLAlchemy
    |
    v
PostgreSQL
```

---

## 📁 Структура проекта

```
src/
 ├── main.py              # Точка входа
 ├── config.py            # Централизованная конфигурация
 ├── mqtt/
 │    └── client.py       # MQTT consumer
 │    └── consumer.py      # Запись данных в БД
 ├── db/
 │    ├── models.py       # ORM модели
 └─── └── session.py      # Async engine / session

migration/
 ├── env.py               # Alembic (async)
 └── versions/

.env.example
README.md
```

---

## 📄 Формат входящих MQTT-сообщений

```json
{
  "device_id": "nrf52840_01",
  "sensor": "sht45",
  "temperature_c": 23.48,
  "humidity_rh": 56.12,
  "ts": 1735728123
}
```

---

## ⚙️ Конфигурация

Все настройки задаются через переменные окружения.

### `.env.example`

```env
# MQTT
MQTT_BROKER=localhost
MQTT_PORT=1883
MQTT_TOPIC=sensors/#

# PostgreSQL
POSTGRES_USERNAME=mqtt
POSTGRES_PASSWORD=mqtt
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mqtt_db
```

Скопируйте и заполните:

```bash
cp .env.example .env
```

---

## 🚀 Установка и запуск

### 1️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Применение миграций

```bash
alembic upgrade head
```

---

### 3️⃣ Запуск сервиса

```bash
 python -m src.main
```

---

## 🧪 Тестовая отправка MQTT-сообщения

```bash
docker run --rm -it eclipse-mosquitto \
  mosquitto_pub \
  -h localhost \
  -p 1883 \
  -t sensors \
  -m '{
    "device_id": "nrf52840_01",
    "sensor": "sht45",
    "temperature_c": 23.48,
    "humidity_rh": 56.12,
    "ts": 1735728123
  }'
```

---

## 🔧 Возможные улучшения

* Batch insert
* Retry / DLQ
* TimescaleDB hypertables
* Pydantic validation
* MQTT QoS / TLS
* Docker Compose (Postgres + Mosquitto)
