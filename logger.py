import csv
import time
from datetime import datetime, timedelta
from os.path import exists

out_path = './out/moisture_log.csv'
headers = ['time', 'adc', 'voltage']

def setup():
    if not exists(out_path):
        with open('./raw_moisture.csv', 'a', newline='') as file:
            # create the csv writer
            writer = csv.writer(file)
            writer.writerow(headers)

def log(adc, voltage):
    with open('./raw_moisture.csv', 'a', newline='') as file:
        now = datetime.now() + timedelta(hours=1)
        current_time = now.strftime("%m-%d-%Y %H:%M:%S")
        
        data = [current_time, adc, voltage]

        print('Logging:', data)
        
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
