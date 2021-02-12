import json

class jsonParser():
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        file = open(self.filename)
        tracks = json.loads(file.read())["tracks"]
        return tracks