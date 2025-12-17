from src.book_class import Book
from src.book_collection import BookCollection
from src.library import Library
from src. random_books import random_book
import random
from src.index_dict import IndexDict

def add_book(lib: Library):
    adding_book = random_book()
    lib.add_book(adding_book)
    print(f'Добавлена книга: {adding_book}')

class CustomIndexDict(IndexDict):
    
    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс
        :param book: Добавляемая книга
        """
        if book.isbn not in self.data:
            self.data[book.isbn] = BookCollection(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса
        :param book: Удаляемая книга
        """
        try:
            self.data[book.isbn].remove(book)
            del self.data[book.isbn]
        except Exception as e:
            print(e)

def delete_book(lib: Library):
    book_for_del = random.choice(lib.book_collection)
    lib.remove_book(book_for_del)
    print(f'Удалена книга: {book_for_del}')

book1 = random_book()
book2 = random_book()
book3 = random_book()

lib = Library()

for i in range(5):
    if not lib:
        print('empty')
        add_book(lib)
    else:
        print('not empty')