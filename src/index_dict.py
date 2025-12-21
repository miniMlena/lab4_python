from collections import UserDict, defaultdict
from typing import Iterator
from src.book_class import Book
from src.book_collection import BookCollection

class IndexDict(UserDict):
    """
    Базовая словарная коллекция для индексации книг
    
    Attributes:
        data (defaultdict): Словарь, где ключи - параметры для индексации,
            значения - объекты BookCollection.
    
    Note:
        Не предназначен для прямого использования. Служит базовым классом
        для специализированных индексов (ISBN, автор, год, жанр).
    """

    def __init__(self):
        self.data = defaultdict(BookCollection)

    def __iter__(self) -> Iterator:
        """
        Создает итератор словарной коллекции
        
        :return: Итератор словарной коллекции
        """
        return iter(self.data)
    
    def __getitem__(self, key) -> BookCollection:
        """
        Находит BookCollection по ключу

        :param key: Ключ, по которому нужно найти значение
        :return: BookCollection, соответствующий ключу (пустой, если ключ не существует)
        """
        return self.data.get(key, BookCollection())
    
    def __len__(self) -> int:
        """
        Возвращает длину словарной коллекции

        :return: Длина словарной коллекции
        """
        return len(self.data)
    
    def __str__(self) -> str:
        """
        Собирает строковое представление словаря

        :return: Строковое представление словаря
        """
        output = []
        for key in self:
            output.append(str(key) + ': ' + str(self[key]))
        return '\n'.join(output)

class ISBNIndexDict(IndexDict):
    """
    Индекс книг по ISBN (уникальный идентификатор)
    
    Args:
        book (Book): Книга для добавления или удаления
    """
    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс

        :param book: Добавляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.isbn not in self.data:
            self.data[book.isbn] = BookCollection(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса

        :param book: Удаляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.isbn in self.data and book in self.data[book.isbn]:
            self.data[book.isbn].remove(book)
            del self.data[book.isbn]

class AuthorIndexDict(IndexDict):
    """
    Индекс книг по авторам
    
    Args:
        book (Book): Книга для добавления или удаления
    """
    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс

        :param book: Добавляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.author not in self.data:
            self.data[book.author] = BookCollection()
        if book not in self.data[book.author]:
            self.data[book.author].add(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса

        :param book: Удаляемая книга
        :return: Данная функция ничего не возвращает
        """
        self.data[book.author].remove(book)
        if not self.data[book.author]:
            del self.data[book.author]

class YearIndexDict(IndexDict):
    """
    Индекс книг по году публикации
    
    Args:
        book (Book): Книга для добавления или удаления
    """
    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс

        :param book: Добавляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.year not in self.data:
            self.data[book.year] = BookCollection()
        if book not in self.data[book.year]:
            self.data[book.year].add(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса

        :param book: Удаляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.year in self.data and book in self.data[book.year]:
            self.data[book.year].remove(book)
            if not self.data[book.year]:
                del self.data[book.year]

class GenreIndexDict(IndexDict):
    """
    Индекс книг по жанру
    
    Args:
        book (Book): Книга для добавления или удаления
    """
    def add(self, book: Book) -> None:
        """
        Добавление книги в индекс

        :param book: Добавляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.genre not in self.data:
            self.data[book.genre] = BookCollection()
        if book not in self.data[book.genre]:
            self.data[book.genre].add(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из индекса

        :param book: Удаляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book.genre in self.data and book in self.data[book.genre]:
            self.data[book.genre].remove(book)
            if not self.data[book.genre]:
                del self.data[book.genre]