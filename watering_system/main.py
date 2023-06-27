import time
import requests
from controllers import valve
from controllers import config
from controllers import moisture
import logger
import os

valve.setup()
logger.setup()

while True:
    logger.log({ 
        "adc": moisture.get_adc(), 
        "voltage": moisture.get_voltage() 
    })

    threshold = config.get_moisture_threshold()

    if threshold is None:
        continue

    if moisture.get_adc() >= threshold:
        print("Moisture is below theshold")
        valve.open(config.get_irrigation_interval())
        valve.close()
    else:
        print("Moisture is above threshold")
    
    time.sleep(config.get_measurement_interval())