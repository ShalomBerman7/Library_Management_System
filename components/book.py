

class Book:
    def __init__(self, id, title, author, is_available):  
        self.title = title
        self.author = author
        self.__id = id
        self.__is_available = is_available

    def __str__(self):
        return f'The Book title: {self.title}, author: {self.author},'

    @property
    def book_id(self):
        return self.__id

    @property
    def is_available(self):
        return self.__is_available

    @is_available.setter
    def is_available(self, val):
        self.__is_available = val

    def to_dict(self):  
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available
        }
        
if __name__ == "__main__":
    book = Book('baby', 'mather', True)
    print(book.book_id)
