import pytest
import builtins
import random
from unittest.mock import patch, MagicMock
#from src.constants import TITLES, AUTHORS, YEARS, GENRES
from src.random_books import random_book, random_book_short
from src.random_simulation import (
    add_book, delete_book, search_by_author, search_by_genre,
    search_by_year, update_author_index, update_year_index,
    get_book_by_combo, get_book_by_isbn, run_simulation
)
from src.book_class import Book
from src.library import Library

class MockConstants:
    TITLES = ["Война и мир", "1984", "Преступление и наказание", "Мастер и Маргарита"]
    AUTHORS = ["Лев Толстой", "Джордж Оруэлл", "Фёдор Достоевский", "Михаил Булгаков"]
    YEARS = [1869, 1949, 1866, 1967]
    GENRES = ["Роман", "Фантастика", "Детектив", "Поэзия"]

# тесты генерации книг
def test_random_book_generation():
    """Тест генерации случайной книги с валидными параметрами"""
    with patch('src.random_books.TITLES', MockConstants.TITLES), \
         patch('src.random_books.AUTHORS', MockConstants.AUTHORS), \
         patch('src.random_books.YEARS', MockConstants.YEARS), \
         patch('src.random_books.GENRES', MockConstants.GENRES):
        random.seed(42)
        book = random_book()
        assert isinstance(book, Book)
        assert book.title in MockConstants.TITLES
        assert book.author in MockConstants.AUTHORS
        assert book.year in MockConstants.YEARS
        assert book.genre in MockConstants.GENRES

def test_random_book_short():
    """Тест генерации случайной пары (название, автор)"""
    with patch('src.random_books.TITLES', MockConstants.TITLES), \
         patch('src.random_books.AUTHORS', MockConstants.AUTHORS):
        random.seed(42)
        title, author = random_book_short()
        assert title in MockConstants.TITLES
        assert author in MockConstants.AUTHORS
        assert isinstance(title, str)
        assert isinstance(author, str)


# ========== Тесты для функций симуляции ==========
def test_add_book_function():
    """Тест функции добавления случайной книги в библиотеку"""
    library = Library()
    initial_len = len(library)
    
    with patch('src.random_simulation.random_book') as mock_random_book:
        mock_book = Book("Тестовая книга", "Тестовый автор", 2023, "Тестовый жанр")
        mock_random_book.return_value = mock_book
        
        add_book(library)
        
        assert len(library) == initial_len + 1
        assert mock_book in library

def test_delete_book_function():
    """Тест функции удаления случайной книги из библиотеки"""
    library = Library()
    book1 = Book("Книга 1", "Автор 1", 2000, "Жанр 1")
    book2 = Book("Книга 2", "Автор 2", 2001, "Жанр 2")
    library.add_book(book1)
    library.add_book(book2)
    initial_len = len(library)
    
    with patch('src.random_simulation.random.choice') as mock_choice:
        mock_choice.return_value = book1
        delete_book(library)
        
        assert len(library) == initial_len - 1
        assert book1 not in library
        assert book2 in library

def test_delete_book_empty_library():
    """Тест удаления из пустой библиотеки"""
    library = Library()
    with patch('src.random_simulation.random.choice') as mock_choice:
        mock_choice.side_effect = IndexError
        try:
            delete_book(library)
        except IndexError:
            pass
        assert len(library) == 0

def test_search_by_author_function():
    """Тест поиска по случайному автору"""
    library = Library()
    book1 = Book("Книга 1", "Толстой", 2000, "Роман")
    book2 = Book("Книга 2", "Достоевский", 2001, "Роман")
    library.add_book(book1)
    library.add_book(book2)
    
    with patch('src.random_simulation.random.choice') as mock_choice, \
         patch('src.random_simulation.AUTHORS', MockConstants.AUTHORS):
        mock_choice.return_value = "Толстой"

        with patch('builtins.print'):
            search_by_author(library)

def test_search_by_genre_function():
    """Тест поиска по случайному жанру"""
    library = Library()
    book = Book("Книга", "Автор", 2000, "Фантастика")
    library.add_book(book)
    
    with patch('src.random_simulation.random.choice') as mock_choice, \
         patch('src.random_simulation.GENRES', MockConstants.GENRES):
        mock_choice.return_value = "Фантастика"
        
        with patch('builtins.print'):
            search_by_genre(library)

def test_search_by_year_function():
    """Тест поиска по случайному году"""
    library = Library()
    book = Book("Книга", "Автор", 2020, "Жанр")
    library.add_book(book)
    
    with patch('src.random_simulation.random.choice') as mock_choice, \
         patch('src.random_simulation.YEARS', MockConstants.YEARS):
        mock_choice.return_value = 2020
        
        with patch('builtins.print'):
            search_by_year(library)

def test_update_author_index_function():
    """Тест обновления автора у случайной книги"""
    library = Library()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман")
    library.add_book(book)
    
    with patch('src.random_simulation.random.choice') as mock_choice, \
         patch('src.random_simulation.AUTHORS', ["Лев Толстой", "Другой Автор"]):

        mock_choice.side_effect = [book, "Другой Автор"]
        
        with patch('builtins.print'):
            update_author_index(library)

        updated_book = next(iter(library))
        assert updated_book.title == "Война и мир"
        assert updated_book.author == "Другой Автор"
        assert updated_book.year == 1869

def test_update_year_index_function():
    """Тест обновления года у случайной книги"""
    library = Library()
    book = Book("1984", "Джордж Оруэлл", 1949, "Фантастика")
    library.add_book(book)
    
    with patch('src.random_simulation.random.choice') as mock_choice, \
         patch('src.random_simulation.YEARS', [1949, 1950, 1951]):
        mock_choice.side_effect = [book, 1950]
        
        with patch('builtins.print'):
            update_year_index(library)

        updated_book = next(iter(library))
        assert updated_book.title == "1984"
        assert updated_book.author == "Джордж Оруэлл"
        assert updated_book.year == 1950

def test_get_book_by_combo_found():
    """Тест получения книги по сочетанию автор-название (книга найдена)"""
    library = Library()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман")
    library.add_book(book)
    initial_len = len(library)
    
    with patch('src.random_simulation.random_book_short') as mock_short:
        mock_short.return_value = ("Война и мир", "Лев Толстой")
        
        with patch('builtins.print'):
            get_book_by_combo(library)
            
        assert len(library) == initial_len - 1  # книга должна быть удалена

def test_get_book_by_combo_not_found():
    """Тест получения книги по сочетанию автор-название (книга не найдена)"""
    library = Library()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман")
    library.add_book(book)
    initial_len = len(library)
    
    with patch('src.random_simulation.random_book_short') as mock_short:
        mock_short.return_value = ("Несуществующая книга", "Неизвестный автор")
        
        with patch('builtins.print'):
            get_book_by_combo(library)
            
        assert len(library) == initial_len  # книга не должна быть удалена

def test_get_book_by_isbn_found():
    """Тест получения книги по ISBN (книга найдена)"""
    library = Library()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман")
    library.add_book(book)
    initial_len = len(library)
    
    with patch('src.random_simulation.random_book') as mock_random_book:
        mock_random_book.return_value = book
        
        with patch('builtins.print'):
            get_book_by_isbn(library)
            
        assert len(library) == initial_len - 1  # Книга должна быть удалена

def test_get_book_by_isbn_not_found():
    """Тест получения книги по ISBN (книга не найдена)"""
    library = Library()
    book = Book("Война и мир", "Лев Толстой", 1869, "Роман")
    library.add_book(book)
    initial_len = len(library)
    
    with patch('src.random_simulation.random_book') as mock_random_book:
        other_book = Book("Другая книга", "Другой автор", 2000, "Другой жанр")
        mock_random_book.return_value = other_book
        
        with patch('builtins.print'):
            get_book_by_isbn(library)
            
        assert len(library) == initial_len  # книга не должна быть удалена

# тесты для run_simulation
def test_run_simulation_with_seed():
    """Тест запуска симуляции с seed"""
    with patch('src.random_simulation.time.sleep'):
        with patch('builtins.print'):
            run_simulation(steps=3, seed=42)

def test_run_simulation_empty_library_always_adds_book():
    """Тест, что при пустой библиотеке в симуляции всегда вызывается add_book."""

    add_book_calls = 0
    original_add_book = add_book
    
    def counted_add_book(lib):
        nonlocal add_book_calls
        add_book_calls += 1
        return original_add_book(lib)
    
    with patch('src.random_simulation.time.sleep'), \
         patch('builtins.print'):

        original_range = builtins.range
        
        def mock_range(*args):
            if len(args) == 1 and args[0] == 10:
                return []
            return original_range(*args)
        
        with patch('builtins.range', side_effect=mock_range), \
             patch('src.random_simulation.add_book', side_effect=counted_add_book), \
             patch('src.random_simulation.random_book') as mock_random_book:
            
            mock_book = MagicMock(spec=Book)
            mock_random_book.return_value = mock_book

            run_simulation(steps=1, seed=42)

            assert add_book_calls == 1

def test_run_simulation_exception_handling():
    """Тест обработки исключений в симуляции"""
    with patch('src.random_simulation.time.sleep'), \
         patch('builtins.print'):

        library = Library()

        with patch('src.random_simulation.Library') as MockLibrary:
            MockLibrary.return_value = library

            with patch('src.random_simulation.random_book') as mock_random_book:
                mock_books = []
                for i in range(10):
                    book = Book(f"Книга {i}", f"Автор {i}", 2000 + i, "Роман")
                    mock_books.append(book)

                mock_random_book.side_effect = mock_books + [Exception("Тестовое исключение")]

                run_simulation(steps=1, seed=42)  # симуляция продолжается после обработки ошибки