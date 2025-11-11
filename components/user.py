from components.book import Book

class User:
    id = 1
    def __init__(self,name, borrowed_books):
        self.__id = User.id
        User.id += 1
        self.__name = name
        self.__borrowed_books = borrowed_books
            
    @property
    def user_id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name    
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name   
    
    def add_borrowed_book(self, book: Book):
        self.__borrowed_books.append(book)
    
    def borrowed_book(self):
        return self.__borrowed_books
    
    def __str__(self):
        return f"id: {self.user_id}, name: {self.name}, list books: {self.borrowed_book()} "

if __name__ == "__main__":
    
    u = User("aa", ['ff', 'dd'])
    print(u.name)
    