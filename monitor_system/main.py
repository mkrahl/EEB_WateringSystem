from flask import Flask, request

app = Flask(__name__)

BASE_ROUTE = "/api/v1"

values = []

@app.route("/", methods=["GET", "POST"])
def state():
    return { "response_code": 200, "data": values }

@app.route("/update", methods=["GET", "POST"])
def state():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        values.append(data)
        return { "response_code": 200 }