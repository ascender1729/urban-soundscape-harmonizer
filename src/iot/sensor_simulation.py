import paho.mqtt.client as mqtt
import json
import time
import random

def simulate_sensor(client, location):
    while True:
        noise_level = random.uniform(30, 90)  # dB
        frequency_distribution = [random.uniform(0, 1) for _ in range(10)]
        
        data = {
            "location": location,
            "noise_level": noise_level,
            "frequency_distribution": frequency_distribution,
            "timestamp": time.time()
        }
        
        client.publish("urban_soundscape/sensor_data", json.dumps(data))
        time.sleep(5)  # Simulate data every 5 seconds

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

simulate_sensor(client, "downtown")
