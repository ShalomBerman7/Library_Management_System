

class Book:
    c_id = 1
    def __init__(self, title, author, is_available):   #=(True/False)
        self.title = title
        self.author = author
        self.__id = Book.c_id
        Book.c_id += 1
        self.__is_available = is_available

    def __str__(self):
        return f'The Book title: {self.title}, author: {self.author},'

    @property
    def book_id(self):
        return self.__id
    
    book_id.setter
    def book_id(self, val):
        self.__id = val

    @property
    def is_available(self):
        return self.__is_available

    is_available.setter
    def is_available(self, val):
        self.__is_available = val

if __name__ == '__main__':
    

    book = Book('baby', 'mather', True)
    print(book.__str__())