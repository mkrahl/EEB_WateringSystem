import json

CONF_PATH = './conf.json'

def get_desired_moisture():
    with open(CONF_PATH, 'r') as f:
        return json.load(f)['desired_moisture']

def set_desired_moisture(moisture):
    with open(CONF_PATH, 'r+') as f:
        data = json.load(f)
        data['desired_moisture'] = moisture
        file.write(json.dumps(data))

def get_moisture_threshold():
    return get_desired_moisture() * 1.1