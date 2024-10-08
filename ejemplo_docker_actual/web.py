from hrid import HRID
from pathlib import Path

from flask import Flask


app = Flask(__name__)
id_generator = HRID('-', ('adjective', 'noun'))
server_id = id_generator.generate()

things_path = Path('./data/things.txt')


@app.route("/")
def home_page():
    try:
        things = things_path.read_text()
    except:
        things = "No things saved!"

    return f"<h1>Demo home page</h1><h3>Server {server_id}</h3><p>Current things:</p><pre>{things}</pre>"


@app.route("/save/<thing>/")
def save(thing):
    with things_path.open('a') as things_file:
        things_file.write(f"saved {thing} from server {server_id}\n")

    return f"<h1>Saved: {thing}</h1><h3>Server {server_id}</h3><a href='/'>Back</a>"


app.run(host="0.0.0.0")
