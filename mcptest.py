import busio
import digitalio
import board
import time
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import csv
from datetime import datetime, timedelta
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

GPIO.setmode(GPIO.BCM)
valve_channel = 21
GPIO.setup(valve_channel, GPIO.OUT)
GPIO.output(valve_channel , 1)
GPIO.setwarnings(False)

def open_valve(seconds):
    GPIO.output(valve_channel , 0)
    time.sleep(seconds)
    GPIO.output(valve_channel , 1)

headers = ['time', 'adc', 'voltage']

with open('./raw_moisture.csv', 'a', newline='') as file:
    # create the csv writer
    writer = csv.writer(file)
    writer.writerow(headers)

open_valve(40)

while True:
    # open the file in the write mode
    with open('./raw_moisture.csv', 'a', newline='') as file:
        now = datetime.now() + timedelta(hours=1)
        current_time = now.strftime("%m:%d:%Y %H:%M:%S")
        data = [current_time, chan.value, chan.voltage]
        
        # create the csv writer
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()

    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    time.sleep(5)