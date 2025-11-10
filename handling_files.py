import json

path = 'data\data.json'

def load_users_data():
    with open(path, 'r') as s:
        return json.load(s)["users"]

def load_books_data():
    with open(path, 'r') as b:
        return json.load(b)["users"]

def write_books_data(data: list):
    with open(path, 'w') as b:
        json.dump(data, b)

def write_users_data(data):
    with open(path, 'w') as s:
        json.dump(data, s)


# write_books_data()
print(load_users_data()["users"])
