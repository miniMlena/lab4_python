from collections import UserDict, defaultdict
from typing import Any, List
from src.book_class import Book
from src.book_collection import BookCollection

class IndexDict(UserDict):

    def __init__(self):
        self.data = defaultdict(BookCollection)

    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, key):
        return self.data.get(key, BookCollection())
    
    def __len__(self) -> int:
        return len(self.data)
    
    def __str__(self): #!!!!!!
        output = []
        for key in self:
            output.append(str(key) + ': ' + str(self[key]))
        return '\n'.join(output)

'''    def contains(self, key: Any) -> bool:
        """Проверить наличие ключа в индексе"""
        return key in self.data
    
    def get_all_keys(self) -> List[Any]:
        """Получить все ключи индекса"""
        return list(self.data.keys())
    '''

class ISBNIndexDict(IndexDict):
    
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
        if book.isbn in self.data and book in self.data[book.isbn]:
            self.data[book.isbn].remove(book)
            del self.data[book.isbn]

class AuthorIndexDict(IndexDict):

    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс
        :param book: Добавляемая книга
        """
        if book.author not in self.data: #Он почему-то добавляет одинаковые книги!!! Хотя вроде нет, но надо проверить
            self.data[book.author] = BookCollection()
        if book not in self.data[book.author]:
            self.data[book.author].add(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса
        :param book: Удаляемая книга
        """
        if book.author in self.data and book in self.data[book.author]:
            self.data[book.author].remove(book)
            if not self.data[book.author]:
                del self.data[book.author]

'''    def find(self, author):
        if author in self.data:
            return self.data[author]
        else:
            return []'''
                

class YearIndexDict(IndexDict):

    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс
        :param book: Добавляемая книга
        """
        if book.year not in self.data:
            self.data[book.year] = BookCollection()
        if book not in self.data[book.year]:
            self.data[book.year].add(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса
        :param book: Удаляемая книга
        """
        if book.year in self.data and book in self.data[book.year]:
            self.data[book.year].remove(book)
            if not self.data[book.year]:
                del self.data[book.year]

class GenreIndexDict(IndexDict):

    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс
        :param book: Добавляемая книга
        """
        if book.genre not in self.data:
            self.data[book.genre] = BookCollection()
        if book not in self.data[book.genre]:
            self.data[book.genre].add(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса
        :param book: Удаляемая книга
        """
        if book.genre in self.data and book in self.data[book.genre]:
            self.data[book.genre].remove(book)
            if not self.data[book.genre]:
                del self.data[book.genre]