from argparse import ArgumentParser
from flask import Flask, request

app = Flask(__name__)

if __name__ == "__main__":
    parser = ArgumentParser(description="Carboff Server")
    parser.add_argument("--debug", "-D", action="store_true",
                        help="enable Flask debug mode")
    parser.add_argument("--port", "-p", default=5000, nargs="?",
                        help="port for Flask server")
    args = parser.parse_args()

    app.run(debug=args.debug, port=args.port)

def parse_post(request, key):
    if request.is_json:
        data = request.get_json()[key]
    else:
        data = request.form.get(key, type=int)

    if type(data) is not int or data < 0:
        return "Error"

    return data

@app.route("/")
def root():
    return {"hello": "world"}

# Input: number of bytes processed by a data center
# Return electricity consumption in kWh
@app.route("/post/datacenter", methods=['POST'])
def data_center():
    data = parse_post(request, 'data')
    if data == "Error":
        return data

    return {"result": 7.2e-11 * data}

# Input: number of bytes processed by watching a video
# Return electricity consumption in kWh
@app.route("/post/video", methods=['POST'])
def video():
    data = parse_post(request, 'data')
    time = parse_post(request, 'time')

    if data != "Error":
        return {"result": 2e-10 * data}
    elif time != "Error":
        return {"result": 4e-3 * time}
    else:
        return "Error"

# Input: number of bytes processed by sending an email
# Return electricity consumption in kWh
@app.route("/post/email", methods=['POST'])
def email():
    data = parse_post(request, 'data')
    time = parse_post(request, 'time')

    if data != "Error":
        return {"result": 5e-10 * data}
    elif time != "Error":
        return {"result": 1.7e-4 * time}
    else:
        return "Error"

# Input: number of bytes processed by network traffic
# Return electricity consumption in kWh
@app.route("/post/network", methods=['POST'])
def network():
    data = parse_post(request, 'data')
    if data == "Error":
        return data

    return {"result": 1.52e-10 * data}

# Input: smartphone usage time in minutes
# Return electricity consumption in kWh
@app.route("/post/smartphone", methods=['POST'])
def smartphone():
    time = parse_post(request, 'time')
    if time == "Error":
        return data

    return {"result": 1.1e-4 * time}

# Input: laptop usage time in minutes
# Return electricity consumption in kWh
@app.route("/post/laptop", methods=['POST'])
def laptop():
    time = parse_post(request, 'time')
    if time == "Error":
        return data

    return {"result": 3.2e-4 * time}
