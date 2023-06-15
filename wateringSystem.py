#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        print(channel)
        if GPIO.input(channel):
                print("Water Detected!")
        else:
                print("NO Water Detected!")

def rising_callback(x):
    print(x)
 
#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=200)
GPIO.add_event_callback(channel, rising_callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)