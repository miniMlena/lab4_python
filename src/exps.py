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

def get_book_by_isbn(lib: Library) -> None:
    '''
    Поиск книги по случайному ISBN
    :param lib: Рассматриваемая библиотека
    :return: Данная функция ничего не возвращает
    '''
    getting_isbn = random.choice(lib.book_collection).isbn
    print(f'Кто-то хочет взять книгу с таким ISBN: {getting_isbn}...')

    suitable_book = lib.find_by_isbn(getting_isbn)
    if suitable_book:
        lib.remove_book(suitable_book[0])
        print('Кто-то получил свою книгу!')
    else:
        print('Такой книги нет в библиотеке')

book1 = random_book()
book2 = random_book()
book3 = random_book()

for i in range(20):
    book = random_book()
    print(book)