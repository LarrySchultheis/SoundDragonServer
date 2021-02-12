import json

class jsonParser():
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        file = open(self.filename)
        obj = json.loads(file.read())
        tracks = obj["tracks"]
        return tracks[0]