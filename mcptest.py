import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import csv
from datetime import datetime
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

headers = ['time', 'adc', 'voltage']

with open('./raw_moisture.csv', 'w', newline='') as file:
     # create the csv writer
    writer = csv.writer(file)
    writer.writerow(headers)
 
while True:
    # open the file in the write mode
    with open('./raw_moisture.csv', 'w', newline='') as file:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data = [current_time, chan.value, chan.voltage]
        
        # create the csv writer
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(data)

    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    time.sleep(5)