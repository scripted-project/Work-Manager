import json

class JSONFile:
    def __init__(self, path, mode='r'):
        try:
            f = open(path, mode)
            self.data = json.load(f)
            self.path = path
        except Exception as e: print(e)

    def save(self):
        try:
            json.dump(self.data, self.path)
        except Exception as e: return