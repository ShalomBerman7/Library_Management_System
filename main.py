from components.user import User
from components.book import Book
from components.library import Library
from utils import manager_file

def print_data(lib):
    for k , v in lib.books.items():
        print(k, v.__str__())
    for k , v in lib.users.items():
        print(k, v.__str__())

def data_initialization() -> Library:
    data_books = manager_file.load_books_data()
    data_users = manager_file.load_users_data()
    
    lib = Library()
    if data_books:
        for book in data_books:
            key = list(book.keys())[0]
            lib.add_book(Book(**book[key]))
    if data_users:
        for user in data_users:
            key = list(user.keys())[0]
            lib.add_user(User(**user[key]))
    return lib

def write_data(lib):
    data = {"users": [], "books": []}
    for k, v in lib.users.items():
            data["users"].append({k: v.to_dict()})
    for k, v in lib.books.items():
        data["books"].append({k: v.to_dict()})
    manager_file.write_data(data)

def main():
    
    lib = data_initialization()
    print_data(lib)
    write_data(lib)
    
if __name__ =="__main__":
    main()
    