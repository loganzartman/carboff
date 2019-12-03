from argparse import ArgumentParser
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return {"hello": "world"}

if __name__ == "__main__":
    parser = ArgumentParser(description="Carboff Server")
    parser.add_argument("--debug", "-D", action="store_true",
                        help="enable Flask debug mode")
    parser.add_argument("--port", "-p", default=5000, nargs="?",
                        help="port for Flask server")
    args = parser.parse_args()

    app.run(debug=args.debug, port=args.port)
