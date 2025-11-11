import json

path = 'data/data.json'

def load_users_data() -> list[dict]:
    with open(path, 'r') as s:
        return json.load(s)["users"]

def load_books_data() -> list[dict]:
    with open(path, 'r') as b:
        return json.load(b)["books"]

def write_data(data: list):
    with open(path, 'w') as b:
        json.dump(data, b)

