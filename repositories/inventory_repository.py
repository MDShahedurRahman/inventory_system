import json
import os


class InventoryRepository:

    FILE_PATH = "data/inventory_data.json"

    def load_data(self):
        if not os.path.exists(self.FILE_PATH):
            return {"products": [], "customers": [], "orders": []}

        with open(self.FILE_PATH, "r") as file:
            return json.load(file)

    def save_data(self, data):
        os.makedirs("data", exist_ok=True)

        with open(self.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)
