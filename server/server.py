from flask import Flask, url_for, render_template
from sounddragon import jsonParser as jp
app = Flask(__name__)

@app.route("/")
def index():
    obj = parse()
    return render_template("index.html", obj=obj)

def parse():
    parser = jp.jsonParser("server/sounddragon/data/tracks.json")
    obj = parser.parse()
    return obj


