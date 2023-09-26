from datetime import datetime
from pathlib import Path

from flask import Flask


app = Flask(__name__)
start = datetime.now()

things_path = Path('./data/things.txt')


@app.route("/")
def home_page():
    return f"<h1>Demo web page (server started at {start})</h1>"


@app.route("/save/<thing>/")
def save(thing):
    with things_path.open('a') as things_file:
        things_file.write(f"saved {thing} at {datetime.now()}\n")

    return f"<h1>Saved: {thing}</h1>"


@app.route("/read/")
def read():
    try:
        things = things_path.read_text()
    except:
        things = "No things saved!"
    return f"<h1>Current things:</h1><pre>{things}</pre>"


app.run(host="0.0.0.0")
