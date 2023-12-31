import csv
import time
from datetime import datetime, timedelta
from os.path import exists
import os

out_path = './out/'
path_to_csv = out_path + 'moisture_log.csv'
headers = ['time', 'adc', 'voltage']

def setup():
    if not exists(out_path):
        os.mkdir(out_path)
    if not exists(path_to_csv):
        with open(path_to_csv, 'a', newline='') as file:
            # create the csv writer
            writer = csv.writer(file)
            writer.writerow(headers)

def log(data):
    with open(path_to_csv, 'a', newline='') as file:
        now = datetime.now() + timedelta(hours=1)
        current_time = now.strftime("%m-%d-%Y %H:%M:%S")
        
        data = [current_time, data['adc'], data['voltage']]

        print('Logging:', data)
        
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
