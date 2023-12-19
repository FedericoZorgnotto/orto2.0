import json
import os


class JSONdatabase:
    def __init__(self, file: str):
        self.path = os.path.dirname(os.path.abspath(__file__)) + "/files/" + file + ".json"

    def get(self, key: str):
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
                return data.get(key)
        except:
            return None

    def set(self, key:str, value:str):
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
                data[key] = value
            with open(self.path, 'w') as f:
                json.dump(data, f)
        except:
            with open(self.path, 'w') as f:
                json.dump({key: value}, f)
    def delete(self, key:str):
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
                del data[key]
            with open(self.path, 'w') as f:
                json.dump(data, f)
        except:
            return None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
