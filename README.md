# ups2mqtt

A simple Python script to publish APC UPS status to an MQTT broker.

## Overview

This script retrieves status information from an APC UPS using `apcaccess` and publishes the parsed data to an MQTT topic. It is useful for integrating UPS status monitoring into home automation systems or dashboards that support MQTT.

## Features
- Fetches UPS status using `apcaccess`
- Publishes status as JSON to a configurable MQTT topic

## Requirements
- Python 3.x
- `apcaccess` command-line tool (part of apcupsd)
- `paho-mqtt` Python package

## Installation
1. Install apcupsd and apcaccess:
   ```bash
   sudo apt-get install apcupsd
   ```
2. Install Python dependencies:
   ```bash
   pip install paho-mqtt
   ```

## Configuration
- Edit the `MQTT_BROKER`, `MQTT_PORT`, and `MQTT_TOPIC` variables in `ups2mqtt.py` to match your MQTT setup.

## Usage
Run the script manually:
```bash
python ups2mqtt.py
```

Or schedule it with cron for periodic updates.

## Running as a systemd Service

To run `ups2mqtt.py` automatically as a background service, you can use systemd.

### 1. Create a systemd Service File
Create a file named `/etc/systemd/system/ups2mqtt.service` with the following content (edit paths and user as needed):

```ini
[Unit]
Description=APC UPS to MQTT Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/mark/ups2mqtt/ups2mqtt.py
WorkingDirectory=/home/mark/ups2mqtt
User=mark
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### 2. Reload systemd and Start the Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable ups2mqtt.service
sudo systemctl start ups2mqtt.service
```

### 3. Check Service Status
```bash
sudo systemctl status ups2mqtt.service
```

This will ensure your script runs automatically in the background and restarts on failure.

## Update Interval

When running as a systemd service, the script will publish UPS status every 1 minute by default. You can change the interval by editing the `UPDATE_INTERVAL` variable in `ups2mqtt.py`.

## Example Output
See `example-output.txt` for a sample MQTT message payload.

## License
MIT
