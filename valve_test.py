import RPi.GPIO as GPIO
import time

channel = 21
GPIO.output(channel , 1)

while True:
    GPIO.output(channel , 1)
    time.sleep(2)
    GPIO.output(channel , 0)