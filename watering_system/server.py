from flask import Flask, request
import config_controller
import moisture_controller

app = Flask(__name__)

BASE_ROUTE = "/api/v1"

@app.route("/calibrate", methods=["POST"])
def calibrate():
    config_controller.set_desired_moisture(
        moisture_controller.get_adc()
    )
    return { "response_code": 200 }