from src.book_class import Book
from src.library import Library
from src. random_books import random_book
import random
from src.constants import AUTHORS, GENRES

def add_book(lib):
    adding_book = random_book()
    lib.add_book(adding_book)
    print(f'Добавлена книга: {adding_book}')

lib = Library()
book1 = random_book()
book2 = random_book()
book3 = random_book()
if not lib.book_collection:
    print('Нет книг для удаления')
else:
    lib.remove_book(book1)
print(lib)


