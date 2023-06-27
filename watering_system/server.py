from flask import Flask, request, Response
from controllers import config
from controllers import moisture
from controllers import valve
import json
from datetime import datetime, timedelta

app = Flask(__name__)

BASE_ROUTE = "/api/v1"


@app.route("/update", methods=["GET"])
def update():
    resp = Response()

    now = datetime.now() + timedelta(hours=1)
    current_time = now.strftime("%m-%d-%Y %H:%M:%S")
    resp.set_data(json.dumps({ 
        "response_code": 200, 
        "data": {
            "moisture": moisture.get_adc(),
            "threshold": config.get_moisture_threshold(),
            "valve_is_open": valve.valve_is_open(),
            "timestamp": current_time
        },
    }))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'

    return resp

@app.route("/calibrate", methods=["POST"])
def calibrate():
    config.set_desired_moisture(
        moisture.get_adc()
    )

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

@app.route("/turn-on", methods=["POST"])
def turn_on():
    config.set_tmp('is_on', True)

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

@app.route("/turn-off", methods=["POST"])
def turn_off():
    config.set_tmp('is_on', False)

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp
