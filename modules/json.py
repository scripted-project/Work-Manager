import json

class JSON:
    def __init__(self, path, mode='r'):
        try:
            f = open(path, mode)
            self.data = json.load(f.read())
            self.path = path
        except Exception as e: return

    def save(self):
        try:
            json.dump(self.data, self.path)
        except Exception as e: return