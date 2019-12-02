from argparse import ArgumentParser
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/")
def root():
    return {"hello": "world"}


if __name__ == "__main__":
    parser = ArgumentParser(description="EcoAPI")
    parser.add_argument("--debug", "-D", action="store_true",
                        help="enable FlaskAPI debug mode")
    args = parser.parse_args()

    app.run(debug=args.debug)
