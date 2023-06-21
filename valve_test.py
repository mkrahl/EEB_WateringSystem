import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
channel = 21
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel , 1)

while True:
    GPIO.output(channel , 1)
    time.sleep(2)
    GPIO.output(channel , 0)