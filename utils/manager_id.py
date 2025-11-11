from random import randint



def create_id(data_ids):
    id = randint(1,10000)
    while id in data_ids:
        id = randint(1,10000)
    return id

