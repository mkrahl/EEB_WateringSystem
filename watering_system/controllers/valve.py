import RPi.GPIO as GPIO
import time

valve_channel = 21

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_channel, GPIO.OUT)
    GPIO.output(valve_channel , 1)

def open(seconds):
    GPIO.output(valve_channel , 0)
    print('Opened valve')
    time.sleep(seconds)

def close():
    GPIO.output(valve_channel , 1)
    print('Closed valve')
