import busio
import digitalio
import board
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import requests
import valve_controller
import config_controller
import logger
import os
from dotenv import load_dotenv

load_dotenv()

MONITORING_SERVER_URL = os.environ.get("MONITORING_SERVER_URL")

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

valve_controller.setup()
logger.setup()

while True:
    data = { "adc": chan.value, "voltage": chan.voltage }
    logger.log(data)

    requests.post(MONITORING_SERVER_URL + "update", json=data, headers={'Content-Type': 'application/json'})

    if chan.value >= config_controller.get_moisture_threshold():
        valve_controller.open(4)
        valve_controller.close()

    time.sleep(5)