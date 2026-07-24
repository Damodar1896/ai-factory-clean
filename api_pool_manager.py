import json
import os
import requests

class APIPoolManager:
    def __init__(self, pool_file="api_pool.json"):
        self.pool_file = pool_file
        self.keys = self.load_keys()
        self.current_index = 0

    def load_keys(self):
        if not os.path.exists(self.pool_file):
            return []
        try:
            with open(self.pool_file, "r") as f:
                data = json.load(f)
                return data.get("api_keys", [])
        except Exception:
            return []

    def get_active_key(self):
        if not self.keys:
            return None
        return self.keys[self.current_index]

    def rotate_key(self):
        if len(self.keys) <= 1:
            return
        self.current_index = (self.current_index + 1) % len(self.keys)
