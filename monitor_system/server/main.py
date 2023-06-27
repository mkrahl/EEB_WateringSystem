from flask import Flask, request, Response
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

app = Flask(__name__)

MICROCONTROLLER_SERVER_URL = os.environ.get("MICROCONTROLLER_SERVER_URL")
BASE_ROUTE = "/api/v1"

@app.route("/update", methods=["GET"])
def update():
    response = requests.get(MICROCONTROLLER_SERVER_URL + "update")
    
    resp = Response()
    resp.set_data(json.dumps(response.json()))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    
    return resp

@app.route("/calibrate", methods=["POST"])
def calibrate():
    requests.post(MICROCONTROLLER_SERVER_URL + "calibrate")

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

@app.route("/reset", methods=["POST"])
def reset():
    requests.post(MICROCONTROLLER_SERVER_URL + "reset")

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp

@app.route("/turn-on", methods=["POST"])
def turn_on():
    requests.post(MICROCONTROLLER_SERVER_URL + "turn-on")

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp

@app.route("/turn-off", methods=["POST"])
def turn_off():
    requests.post(MICROCONTROLLER_SERVER_URL + "turn-off")

    resp = Response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp
