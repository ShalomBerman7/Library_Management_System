from components.user import User
from components.book import Book
from components.library import Library
from utils import manager_file




def main():
    data_books = manager_file.load_books_data()
    data_users = manager_file.load_users_data()
    lib = Library()
    for v in data_books.values():
        book = Book(v['title'], v['author'], v['is_available'])
        lib.add_book(book)
        
    for v in data_users.values():
        lib.add_user(User(v['name'], v['borrowed_books']))

    def print_books():
        for k , v in lib.books.items():
            print(k, v.__str__())
    def print_users():
        for k , v in lib.users.items():
            print(k, v.__str__())
    print_users()
    
if __name__ =="__main__":
    main()