import json
import os

class JsonManager:
    def __init__(self, filename):
        self.filename = f"{filename}.json"
        self.path = f"core/data/{filename}.json"

    def read_file(self):
        if os.path.getsize(filename=self.path) > 0:
            with open(file=self.path, mode="r", encoding="UTF-8") as file:
                return json.load(file)
        else:
            return {}

    def write_file(self, data: dict):
        with open(file=self.path, mode="w", encoding="UTF-8") as file:
            return json.dump(data, file, indent=4)

    def append(self, new_data: list):
        current_data = self.read_file()
        if not isinstance(current_data, dict):
            current_data = {}
        current_data.update(new_data)  # Merge dictionaries
        self.write_file(current_data)

    def generate_new_id(self):
        data = self.read_file()
        if data:
            return max(item.get("id", 0) for item in data) + 1
        return 1
    
