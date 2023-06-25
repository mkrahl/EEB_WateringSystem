import json

def get_desired_moisture():
    with open('./conf.json', 'r') as f:
        return json.load(f)['desired_moisture']

def set_desired_moisture():
    yield

def get_moisture_threshold():
    return get_desired_moisture() * 1.1