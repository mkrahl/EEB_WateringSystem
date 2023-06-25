from flask import Flask, request

app = Flask(__name__)

BASE_ROUTE = "/api/v1"

@app.route("/", methods=["GET", "POST"])
def state():
    return { "response_code": 200 }