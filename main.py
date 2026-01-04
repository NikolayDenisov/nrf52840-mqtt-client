import asyncio
from src.mqtt.client import start_mqtt
from src.mqtt.consumer import consume


async def main():
    queue = asyncio.Queue()

    loop = asyncio.get_running_loop()
    start_mqtt(loop, queue)

    await consume(queue)


if __name__ == "__main__":
    asyncio.run(main())
