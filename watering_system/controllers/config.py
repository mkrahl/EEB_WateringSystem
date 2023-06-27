import json

CONF_PATH = './conf.json'
TMP = './tmp'

def get_desired_moisture():
    with open(CONF_PATH, 'r') as f:
        return json.load(f)['desired_moisture']

def set_desired_moisture(moisture):
    with open(CONF_PATH, 'r+') as f:
        data = json.load(f)
        data['desired_moisture'] = moisture
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()

def get_moisture_threshold():
    desired_moisture = get_desired_moisture()
    
    if desired_moisture is None:
        return None

    return get_desired_moisture() * 1.1

def get_measurement_interval():
    with open(CONF_PATH, 'r') as f:
        return json.load(f)['measurement_interval']

def get_irrigation_interval():
    with open(CONF_PATH, 'r') as f:
        return json.load(f)['irrigation_interval']

def get_tmp(key):
    with open(TMP, 'r') as f:
        try:
            value = json.load(f)[key]
            return value
        except KeyError:
            return None

def set_tmp(key, value):
    with open(TMP, 'r+') as f:
        data = json.load(f)
        data[key] = value
        f.seek(0)
        f.write(json.dumps(data))
        f.truncate()