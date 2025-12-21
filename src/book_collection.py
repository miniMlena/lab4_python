from typing import Iterator, List, Union
from src.book_class import Book

class BookCollection():
    """
    Списковая коллекция объектов Book
    
    Args:
        *books: Произвольное количество объектов Book для добавления при создании
    
    Attributes:
        books_list (List[Book]): Список объектов Book

    Raises:
        ValueError: При попытке удалить несуществующую книгу методом remove()
    """
    def __init__(self, *books):
        self.books_list: List[Book] = []

        for book in books:
            self.add(book)
    
    def __getitem__(self, key: int | slice) -> Union[Book, 'BookCollection']:
        """
        Получение элемента или среза коллекции по ключу

        :param key: Ключ для получения элементов
        :type key: int | slice
        :return: Элемент или срез коллекции
        :rtype: Book | BookCollection
        """
        if isinstance(key, slice):
            return BookCollection(*self.books_list[key])
        return self.books_list[key]
    
    def __iter__(self) -> Iterator:
        """
        Создает итератор по коллекции

        :return: Итератор по коллекции
        :rtype: Iterator
        """
        return iter(self.books_list)
    
    def __len__(self) -> int:
        """
        Возвращает длину коллекции

        :return: Длина коллекции
        :rtype: int
        """
        return len(self.books_list)
    
    def __contains__(self, book: Book) -> bool:
        """
        Определяет, есть ли книга в коллекции

        :param book: Книга, наличие котрой нужно проверить
        :return: Предикат наличия книги в коллекции
        :rtype: bool
        """
        return book in self.books_list
    
    def __repr__(self) -> str:
        """
        Создает строковое представление коллекции для отладки

        :return: Отладочное строковое представление коллекции
        :rtype: str
        """
        output = []
        for book in self:
            output.append(book.__repr__() + ',')
        return '\n'.join(output)
    
    def __str__(self) -> str:
        """
        Создает строковое представление коллекции

        :return: Строковое представление коллекции
        :rtype: str
        """
        output = []
        for book in self:
            output.append(book.__str__())
        return '\n'.join(output)

    def add(self, book: Book) -> None:
        """
        Добавление книги в коллекцию

        :param book: Книга для добавления
        :return: Данная функция ничего не возвращает
        """
        self.books_list.append(book)

    def remove(self, book: Book) -> None:
        """
        Удаление книги из коллекции

        :param book: Книга для удаления
        :return: Данная функция ничего не возвращает
        """
        if book in self:
            self.books_list.remove(book)
        else:
            raise ValueError(f'Такой книги нет в коллекции: {book}')