from user import User
from book import Book

class Library:
    
    def __init__(self, books=None, users=None):
        self.books = books
        self.users = users

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_user(self, user:User):
        self.users[user.user_id] = user

    def borrow_book(self, user_id, book_id):
        if Book.is_available:    
            Book.is_available = False 

    def return_book(self, user_id, book_id):
        Book.is_available = True

    def list_available_books(self) -> dict:
        pass

    def search_book(self, title):
        pass
    