import json
import os

FILE_PATH = "data/database.json"


def load_data():

    if not os.path.exists(FILE_PATH):
        return {"managers": []}

    try:

        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {"managers": []}


def save_data(data):

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)