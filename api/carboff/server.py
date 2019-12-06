from argparse import ArgumentParser
from flask import Flask, request, jsonify

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

# Custom Exception used for returning meaningful messages to API requests
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv

# Handler for InvalidUsage exceptions
@app.errorhandler(InvalidUsage)
def handleError(e):
    # Parse error and send it to the user in a response
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response

@app.route("/", methods=["GET"])
def root():
    return {"hello": "world"}

# Receives POST requests containing data usage metrics
# Returns the user's impact on the environment
@app.route("/impact/action", methods=["POST"])
def impact_action():
    if request is None or not request.is_json:
        raise InvalidUsage('Request is in an invalid state', status_code=400)

    try:
        data = request.json["data"]
        duration = request.json["duration"]
        location = request.json["location"]
        device_type = request.json["device_type"]
        network_type = request.json["network_type"]
    except: # The proper fields were not provided in the request
        raise InvalidUsage('Required: data, duration, location, device_type, and network_type', status_code=400)

    return impact.action(
        data=data,
        duration=duration,
        location=location,
        device_type=device_type,
        network_type=network_type
    )

if __name__ == "__main__":
    main()
