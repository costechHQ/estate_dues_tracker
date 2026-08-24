import json
import os

DATA_FILE = "data.json"

def load_data():
    """returns an empty dictionary instead of crashing"""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Saved data could not be read")
        return {}
    

def save_data(data):
    """takes our python dictionary and writes it into"""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("The data could not be saved.")