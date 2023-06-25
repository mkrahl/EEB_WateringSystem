from flask import Flask, request

app = Flask(__name__)

BASE_ROUTE = "/api/v1"

@app.route("/calibrate", methods=["POST"])
def calibrate():
    return { "response_code": 200 }