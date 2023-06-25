from flask import Flask, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

MICROCONTROLLER_SERVER_URL = os.environ.get("MICROCONTROLLER_SERVER_URL")
BASE_ROUTE = "/api/v1"

values = []

@app.route("/", methods=["GET"])
def index():
    return { "response_code": 200, "data": values }

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    print(data)
    values.append(data)
    return { "response_code": 200 }

@app.route("/calibrate", methods=["POST"])
def state():
    requests.post(MICROCONTROLLER_SERVER_URL + "calibrate")
    return { "response_code": 200 }
