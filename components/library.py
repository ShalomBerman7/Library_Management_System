from components.user import User
from components.book import Book

class Library:
    
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book: Book):
        self.books[book.book_id] = book
        
    def add_user(self, user:User):
        self.users[user.user_id] = user
        
    def borrow_book(self, user_id, book_id):
        if self.books[book_id].is_available:
            self.books[book_id].is_available = False
            self.users[user_id].add_borrowed_book(book_id)
            return 'הספר הושאל בהצלחה'
        else:
            return 'הספר לא זמין להשאלה'

    def return_book(self, user_id, book_id):
        self.books[book_id].is_available = True
        self.users[user_id].pop(book_id)


    def available_books(self) -> list:
        books_available = []
        for book in self.books.values():
            if book.is_available:
                books_available.append(book)
        return books_available

    def search_book(self, title):
        books_by_title = []
        for book in self.books.values():
            if book["title"] == title:
                books_by_title.append(book)
        return books_by_title
    
