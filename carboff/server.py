from argparse import ArgumentParser
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    return {"hello": "world"}

@app.route("/post/datacenter/json", methods=['POST'])
def data_center_json():
    data = request.get_json()['data']
    return data_center(data)

@app.route("/post/datacenter", methods=['POST'])
def data_center_form():
    data = request.form.get('data', type=int)
    return data_center(data)

# Input: number of bytes processed by a data center
# Return electricity consumption in KwH
def data_center(data):
    if data is None or data < 0:
        return "Error"

    return {"result": 7.2e-11 * data}

if __name__ == "__main__":
    parser = ArgumentParser(description="Carboff Server")
    parser.add_argument("--debug", "-D", action="store_true",
                        help="enable Flask debug mode")
    parser.add_argument("--port", "-p", default=5000, nargs="?",
                        help="port for Flask server")
    args = parser.parse_args()

    app.run(debug=args.debug, port=args.port)
