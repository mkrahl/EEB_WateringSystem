import time
import requests
from controllers import valve
from controllers import config
from controllers import moisture
import logger
import os

valve.setup()
logger.setup()

def sleep():
    time.sleep(config.get_measurement_interval())

try:
    while True:
        is_on = config.get_tmp('is_on')

        if not is_on:
            sleep()
            continue

        logger.log({ 
            "adc": moisture.get_adc(), 
            "voltage": moisture.get_voltage() 
        })

        threshold = config.get_moisture_threshold()

        if threshold is None:
            sleep()
            continue

        if moisture.get_adc() >= threshold:
            print("Moisture is below theshold")
            valve.open(config.get_irrigation_interval())
            valve.close()
        else:
            print("Moisture is above threshold")
        
        sleep()
except: 
    valve.close()