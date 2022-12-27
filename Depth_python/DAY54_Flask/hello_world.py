from flask import Flask
from pickle import TRUE


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1> Hello, Wordl! </h1>"


if __name__ == "__main__":
    app.run(debug=TRUE)  # dont use this on production
