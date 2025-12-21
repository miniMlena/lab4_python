from typing import Iterator
from src.book_class import Book
from src.book_collection import BookCollection
from src.index_dict import ISBNIndexDict, AuthorIndexDict, YearIndexDict, GenreIndexDict

class Library:
    """
    Библиотека книг с поддержкой индексации по различным параметрам
    
    Attributes:
        book_collection (BookCollection): Основная коллекция всех книг в библиотеке
        isbn_index (ISBNIndexDict): Индекс книг по ISBN
        author_index (AuthorIndexDict): Индекс книг по авторам
        year_index (YearIndexDict): Индекс книг по году публикации
        genre_index (GenreIndexDict): Индекс книг по жанру
    """
    def __init__(self):
        self.book_collection = BookCollection()

        self.isbn_index = ISBNIndexDict()
        self.author_index = AuthorIndexDict()
        self.year_index = YearIndexDict()
        self.genre_index = GenreIndexDict()

    def __len__(self) -> int:
        """
        Возвращает количество книг в библиотеке

        :return: Количество книг в библиотеке
        :rtype: int
        """
        return self.book_collection.__len__()
    
    def __iter__(self) -> Iterator[Book]:
        """
        Создает итератор по библиотеке

        :return: Итератор по библиотеке
        :rtype: Iterator
        """
        return self.book_collection.__iter__()
 
    def __str__(self) -> str:
        """
        Создает строковое представление бибилотеки

        :return: Строковое представление библиотеки
        :rtype: str
        """
        return self.book_collection.__str__()

    def add_book(self, book: Book) -> None:
        """
        Добавление книги в библиотеку

        :param book: Добавляемая книга
        :return: Данная функция ничего не возвращает
        """
        if book not in self.book_collection:
            self.isbn_index.add(book)
            self.author_index.add(book)
            self.year_index.add(book)
            self.genre_index.add(book)

        self.book_collection.add(book)

    def remove_book(self, book: Book) -> None:
        """
        Удаление книги из библиотеки

        :param book: Удаляемая книга
        :return: Данная функция ничего не возвращает
        """
        self.book_collection.remove(book)
        
        if book not in self.book_collection:
            self.isbn_index.remove(book)
            self.author_index.remove(book)
            self.year_index.remove(book)
            self.genre_index.remove(book)

    def find_by_author(self, author: str) -> BookCollection:
        """
        Поиск книг данного автора в библиотеке

        :param author: Автор для поиска
        :type author: str
        :return: Коллекция книг этого автора
        :rtype: BookCollection
        """
        return self.author_index[author]
        
    def find_by_genre(self, genre: str) -> BookCollection:
        """
        Поиск книг данного жанра в библиотеке

        :param genre: Жанр для поиска
        :type genre: str
        :return: Коллекция книг этого жанра
        :rtype: BookCollection
        """
        return self.genre_index[genre]
    
    def find_by_year(self, year: int) -> BookCollection:
        """
        Поиск книг данного года выпуска в библиотеке

        :param year: Год для поиска
        :type year: str
        :return: Коллекция книг этого года выпуска
        :rtype: BookCollection
        """
        return self.year_index[year]
    
    def find_by_isbn(self, isbn: str) -> BookCollection:
        """
        Поиск книг с указанным ISBN в библиотеке

        :param isbn: ISBN для поиска
        :type isbn: str
        :return: Коллекция книг с таким ISBN
        :rtype: BookCollection
        """
        return self.isbn_index[isbn]