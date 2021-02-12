from flask import Flask, url_for, render_template
from sounddragon import jsonParser as jp
app = Flask(__name__)

@app.route("/")
def index():
    tracks = parse()
    print(tracks)
    return render_template("index.html", tracks=tracks)

def parse():
    parser = jp.jsonParser("server/sounddragon/data/tracks.json")
    tracks = parser.parse()
    return tracks


