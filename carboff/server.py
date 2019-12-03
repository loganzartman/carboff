from argparse import ArgumentParser
from flask import Flask, request

import carboff.impact as impact

app = Flask(__name__)

def main():
    parser = ArgumentParser(description="Carboff Server")
    parser.add_argument("--debug", "-D", action="store_true",
                        help="enable Flask debug mode")
    parser.add_argument("--port", "-p", default=5000, nargs="?",
                        help="port for Flask server")
    args = parser.parse_args()

    app.run(debug=args.debug, port=args.port)

@app.route("/", methods=["GET"])
def root():
    return {"hello": "world"}

@app.route("/impact/action", methods=["GET"])
def impact_action():
    data = request.json["data"]
    duration = request.json["duration"]
    location = request.json["location"]
    device_type = request.json["device_type"]
    network_type = request.json["network_type"]

    return impact.action(
        data=data,
        duration=duration,
        location=location,
        device_type=device_type,
        network_type=network_type
    )

if __name__ == "__main__":
    main()
