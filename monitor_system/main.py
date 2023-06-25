from flask import Flask, request

app = Flask(__name__)

BASE_ROUTE = "/api/v1"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return { "response_code": 200, "message": "index" }

    if request.method == "POST":
        req = request.json
        print(req)