from typing import Union, List
from src.book_class import Book

class BookCollection():
    """
    
    """
    def __init__(self, *books):
        self.books_list: List[Book] = []

        for book in books:
            self.add(book)
    
    def __getitem__(self, key: Union[int, slice]) -> Union[Book, 'BookCollection']:
        if isinstance(key, slice):
            return BookCollection(self.books_list[key])
        return self.books_list[key]
    
    def __iter__(self):
        return iter(self.books_list)
    
    def __len__(self):
        return len(self.books_list)
    
    def __contains__(self, book):
        return book in self.books_list
    
    def __repr__(self):
        output = []
        for book in self:
            output.append(book.__repr__() + ',')
        return '\n'.join(output)
    
    def __str__(self):
        output = []
        for book in self:
            output.append(book.__str__())
        return '\n'.join(output)

    def add(self, book: Book):
        self.books_list.append(book)

    def remove(self, book: Book):
        if book in self:
            self.books_list.remove(book)
        else:
            raise ValueError(f'Такой книги нет в коллекции: {book}')