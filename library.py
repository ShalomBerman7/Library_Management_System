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
        if self.books[book_id].is_available:
            self.books[book_id].is_available = False
            self.users[user_id].add_borrowed_book(book_id)    #לבדוק!
            return 'הספר הושאל בהצלחה'
        else:
            return 'הספר לא זמין להשאלה'

    def return_book(self, user_id, book_id):
        self.books[book_id].is_available = True
        self.users[user_id].pop(book_id)

    def list_available_books(self) -> dict:
        pass

    def search_book(self, title):
        pass
    