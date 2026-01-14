from src.db.session import AsyncSessionLocal
from src.db.models import SensorData


async def consume(queue):
    async with AsyncSessionLocal() as session:
        while True:
            data = await queue.get()
            if not isinstance(data, dict):
                continue
            if "ts" not in data:
                continue

            obj = SensorData(
                device_id=data["device_id"],
                sensor=data["sensor"],
                temperature_c=data["temperature_c"],
                humidity_rh=data["humidity_rh"],
                ts=data["ts"],
            )

            session.add(obj)
            await session.commit()
