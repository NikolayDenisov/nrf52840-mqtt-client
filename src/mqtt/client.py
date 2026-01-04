import json
import asyncio
import paho.mqtt.client as mqtt
from src.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC


def start_mqtt(loop: asyncio.AbstractEventLoop, queue: asyncio.Queue):

    def on_connect(client, userdata, flags, rc):
        print("MQTT connected:", rc)
        client.subscribe(MQTT_TOPIC)

    def on_message(client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            asyncio.run_coroutine_threadsafe(
                queue.put(payload),
                loop,
            )
        except Exception as e:
            print("MQTT parse error:", e)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT)
    client.loop_start()

    return client
