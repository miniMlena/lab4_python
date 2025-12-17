from typing import Union, List, Dict
from collections import defaultdict
from src.book_class import Book

class BookCollection():
    """
    
    """
    def __init__(self, *books):
        self.books_counter: Dict[Book, int] = defaultdict(int)
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
    
    book_count_dict = {}

    def add(self, book: Book):
        self.books_list.append(book)
        self.books_counter[book] += 1

    def remove(self, book: Book):
        if book in self.books_list: # book in self?
            self.books_list.remove(book) # Удалит только первое вхождение, т.е. если было нескольколько экземпляров, остальные останутся
        else:
            raise ValueError(f'Такой книги нет в коллекции: {book}')
        
        self.books_counter[book] -= 1
        if self.books_counter[book] == 0:
            del self.books_counter[book]
        
"""    def remove_by_isbn(self, isbn):
        for book in self.books_list:
            if book.isbn == isbn:
                self.remove(book)
                break
        else:
            raise ValueError(f'Книги с таким ISBN нет в коллекции: {isbn}')
        
    def remove_by_combination(self, title, author, year):
        for book in self.books_list:
            if book.title == title and book.author == author and book.year == year:
                self.remove(book)
                break
        else:
            raise ValueError(f'Книги с такими параметрами нет в коллекции: {author} "{title}" {year}')"""


'''from src.random_generation import random_book
bc = BookCollection()

bc.add(random_book())
bc.add(random_book())
bc.add(random_book())
print(bc)
print(repr(bc))'''