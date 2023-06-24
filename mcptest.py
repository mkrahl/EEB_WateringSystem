import busio
import digitalio
import board
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import valve_controller
import logger

import json

def get_moisture_theshold():
    with open('./conf.json', 'r') as f:
        conf = json.load(f)
        print(conf)
        return conf.moisture_threshold

print(get_moisture_theshold())

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

watered = False

while True:
    logger.log(chan.value, str(chan.voltage) + 'V')

    if not watered:
        valve_controller.open(40)
        valve_controller.close()
        watered = True

    time.sleep(5)