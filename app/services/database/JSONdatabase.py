import json
import os
class JSONdatabase:
    def __init__(self, path):
        self.path = path+".json"
        self.data = {}
        self.load()
    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.data = json.load(f)
    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)
    def get(self, key):
        return self.data.get(key)
    def set(self, key, value):
        self.data[key] = value
        self.save()
    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()
    def get_all(self):
        return self.data
    def delete_all(self):
        self.data = {}
        self.save()
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)