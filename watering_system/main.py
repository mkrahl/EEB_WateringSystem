import time
import requests
from controllers import valve
from controllers import config
from controllers import moisture
import logger
import os
from dotenv import load_dotenv

load_dotenv()

MONITORING_SERVER_URL = os.environ.get("MONITORING_SERVER_URL")

valve.setup()
logger.setup()

while True:
    data = { "adc": moisture.get_adc(), "voltage": moisture.get_voltage() }
    logger.log(data)

    if moisture.get_adc() >= config.get_moisture_threshold():
        print("Moisture is below theshold")
        valve.open(4)
        valve.close()
    else:
        print("Moisture is above threshold")
    
    time.sleep(5)