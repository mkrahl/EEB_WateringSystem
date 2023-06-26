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

    if moisture.get_adc() >= config.get_moisture_threshold():
        print("Moisture is below theshold")
        valve.open(4)
        valve.close()
    else:
        print("Moisture is above threshold")
    
    time.sleep(5)