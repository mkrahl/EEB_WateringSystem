import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
channel = 21
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel , 1)
GPIO.setwarnings(False)
while True:
    print("off")
    GPIO.output(channel , 1)
    time.sleep(10)
    print("on")
    GPIO.output(channel , 0)