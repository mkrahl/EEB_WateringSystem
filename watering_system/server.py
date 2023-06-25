from flask import Flask, request
import config_controller
import moisture_controller

app = Flask(__name__)

BASE_ROUTE = "/api/v1"

headers = {
    'access-control-allow-origin': '*'
}

@app.route("/update", methods=["GET"])
def update():
    return { 
        "response_code": 200, 
        "data": { 
            "moisture": moisture_controller.get_adc() 
        },
        "headers": headers
    }

@app.route("/calibrate", methods=["POST"])
def calibrate():
    config_controller.set_desired_moisture(
        moisture_controller.get_adc()
    )
    return { 
        "response_code": 200,
        "headers": headers 
    }