import json
import os

class JsonManager:
    def __init__(self, filename):
        self.filename = f"{filename}.json"
        self.path = f"data/{filename}.json"

    def read_file(self):
        if os.path.getsize(filename=self.path) > 0:
            with open(file=self.path, mode="r", encoding="UTF-8") as file:
                return json.load(file)
        else:
            return list()

    def write_file(self, data: list):
        with open(file=self.path, mode="w", encoding="UTF-8") as file:
            return json.dump(data, file, indent=4)

    def append(self, data: list):
        if not os.path.exists(self.path):
            current_data = []
        else:
            with open(self.path, mode="r", encoding="UTF-8") as file:
                current_data = json.load(file)
        current_data.append(data)

        with open(self.path, mode="w", encoding="utf-8") as file:
            json.dump(current_data, file, indent=4)

    def generate_new_id(self):
        data = self.read_file()
        if data:
            return max(item.get("id", 0) for item in data) + 1
        return 1
