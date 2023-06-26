import RPi.GPIO as GPIO
import time

valve_channel = 21
is_open = False

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_channel, GPIO.OUT)
    GPIO.output(valve_channel , 1)

def open(seconds):
    global is_open
    GPIO.output(valve_channel , 0)
    is_open = True
    print('Opened valve')
    time.sleep(seconds)

def close():
    global is_open
    GPIO.output(valve_channel , 1)
    is_open = False
    print('Closed valve')

def valve_is_open():
    global is_open
    print("valve is opened: ", is_open)
    return is_open
