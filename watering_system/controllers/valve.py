import RPi.GPIO as GPIO
import time
from controllers import config

valve_channel = 21

TMP = './tmp'

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_channel, GPIO.OUT)
    GPIO.output(valve_channel , 1)

def open(seconds):
    global is_open
    GPIO.output(valve_channel , 0)
    config.set_tmp('is_open', True)
    print('Opened valve')
    time.sleep(seconds)

def close():
    global is_open
    GPIO.output(valve_channel , 1)
    config.set_tmp('is_open', False)
    print('Closed valve')

def valve_is_open():
    return config.get_tmp('is_open')
