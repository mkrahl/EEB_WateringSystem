from flask import Flask, request, Response
import config_controller
import moisture_controller
import json
from datetime import datetime, timedelta

app = Flask(__name__)

BASE_ROUTE = "/api/v1"

headers = {
    'Access-Control-Allow-Origin': '*'
}

@app.route("/update", methods=["GET"])
def update():
    resp = Response()

    now = datetime.now() + timedelta(hours=1)
    current_time = now.strftime("%m-%d-%Y %H:%M:%S")
    resp.set_data(json.dumps({ 
        "response_code": 200, 
        "data": {
            "moisture": moisture_controller.get_adc(),
            "threshold": config_controller.get_moisture_threshold(),
            "timestamp": current_time
        },
    }))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route("/calibrate", methods=["POST"])
def calibrate():
    config_controller.set_desired_moisture(
        moisture_controller.get_adc()
    )
    return { 
        "response_code": 200,
        "headers": headers 
    }