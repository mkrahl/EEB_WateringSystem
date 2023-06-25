import time
import requests
import valve_controller
import config_controller
import moisture_controller
import logger
import os
from dotenv import load_dotenv

load_dotenv()

MONITORING_SERVER_URL = os.environ.get("MONITORING_SERVER_URL")

valve_controller.setup()
logger.setup()

while True:
    data = { "adc": moisture_controller.get_adc(), "voltage": moisture_controller.get_voltage() }
    logger.log(data)

    requests.post(MONITORING_SERVER_URL + "update", json=data, headers={'Content-Type': 'application/json'})

    if chan.value >= config_controller.get_moisture_threshold():
        valve_controller.open(4)
        valve_controller.close()

    time.sleep(5)