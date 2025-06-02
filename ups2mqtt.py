import subprocess
import json
import paho.mqtt.client as mqtt
import time

# MQTT configuration
MQTT_BROKER = "mqtt.local"      # Change to your broker address
MQTT_PORT = 1883
MQTT_TOPIC = "ups/server-status"
MQTT_USERNAME = "your_username"  # Set your MQTT username
MQTT_PASSWORD = "your_password"  # Set your MQTT password

def get_apc_status():
    result = subprocess.run(['apcaccess', 'status'], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    return data

def publish_to_mqtt(data):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    payload = json.dumps(data)
    client.publish(MQTT_TOPIC, payload)
    client.disconnect()

if __name__ == "__main__":
    UPDATE_INTERVAL = 60  # seconds
    while True:
        status = get_apc_status()
        publish_to_mqtt(status)
        time.sleep(UPDATE_INTERVAL)