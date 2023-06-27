import RPi.GPIO as GPIO
import time

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
    with open(TMP, 'r+') as f:
        data = json.load(f)
        data['is_open'] = True
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()
    print('Opened valve')
    time.sleep(seconds)

def close():
    global is_open
    GPIO.output(valve_channel , 1)
    with open(TMP, 'r+') as f:
        data = json.load(f)
        data['is_open'] = False
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()
    print('Closed valve')

def valve_is_open():
    with open(CONF_PATH, 'r') as f:
        return json.load(f)['is_open']
