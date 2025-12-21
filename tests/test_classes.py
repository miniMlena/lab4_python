import pytest
from src.book_class import Book
from src.book_collection import BookCollection
from src.index_dict import IndexDict, ISBNIndexDict, AuthorIndexDict, YearIndexDict, GenreIndexDict
from src.library import Library

# тесты для класса Book
def test_book_initialization():
    """Тест корректной инициализации объекта Book"""
    book = Book("Война и мир", "Лев Толстой", 1869, "роман")
    assert book.title == "Война и мир"
    assert book.author == "Лев Толстой"
    assert book.year == 1869
    assert book.genre == "роман"
    assert hasattr(book, 'isbn') and book.isbn is not None

def test_book_str():
    """Тест строкового представления"""
    book = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "роман")
    str_repr = book.__str__()
    assert "Фёдор Достоевский" in str_repr
    assert "Преступление и наказание" in str_repr
    assert "1866" in str_repr
    assert "ISBN:" in str_repr

def test_book_isbn_calculation():
    """Тест расчета ISBN на основе метаданных книги"""
    book1 = Book("Анна Каренина", "Лев Толстой", 1878, "роман")
    book2 = Book("Анна Каренина", "Лев Толстой", 1878, "роман")
    book3 = Book("Война и мир", "Лев Толстой", 1869, "роман")
    assert book1.isbn == book2.isbn
    assert book1.isbn != book3.isbn

# тесты для BookCollection
def test_bookcollection_initialization():
    """Тест инициализации BookCollection с книгами"""
    book1 = Book("Книга1", "Автор1", 2000, "жанр1")
    book2 = Book("Книга2", "Автор2", 2001, "жанр2")
    collection = BookCollection(book1, book2)
    assert len(collection) == 2
    assert book1 in collection
    assert book2 in collection

def test_bookcollection_add_and_remove():
    """Тест добавления и удаления книг из коллекции"""
    book = Book("Книга", "Автор", 2025, "жанр")
    collection = BookCollection()
    collection.add(book)
    assert book in collection
    assert len(collection) == 1
    collection.remove(book)
    assert book not in collection
    assert len(collection) == 0

def test_bookcollection_remove_nonexistent():
    """Тест удаления несуществующей книги"""
    book = Book("Книга", "Автор", 2025, "жанр")
    collection = BookCollection()
    with pytest.raises(ValueError, match="Такой книги нет в коллекции"):
        collection.remove(book)

def test_bookcollection_getitem_slice():
    """Тест получения среза из коллекции"""
    books = [Book(f"Книга{i}", f"Автор{i}", 2000+i, "жанр") for i in range(5)]
    collection = BookCollection(*books)
    slice_result = collection[1:3]
    assert isinstance(slice_result, BookCollection)
    assert len(slice_result) == 2
    assert books[1] in slice_result
    assert books[2] in slice_result

def test_bookcollection_iteration():
    """Тест итерации по коллекции"""
    books = [Book(f"Книга{i}", f"Автор{i}", 2000+i, "жанр") for i in range(3)]
    collection = BookCollection(*books)
    iterated_books = list(collection)
    assert iterated_books == books

# тесты для IndexDict и его производных
def test_indexdict_getitem():
    """Тест получения значения из IndexDict по ключу"""
    index = IndexDict()
    result = index["несуществующий_ключ"]
    assert isinstance(result, BookCollection)
    assert len(result) == 0

def test_indexdict_str():
    """Тест строкового представления IndexDict"""
    book = Book("Книга", "Автор", 2025, "жанр")
    index = IndexDict()
    index.data["ключ"] = BookCollection(book)
    str_repr = str(index)
    assert "ключ" in str_repr
    assert "Книга" in str_repr or "Автор" in str_repr

def test_isbnindex_add_remove():
    """Тест добавления и удаления в ISBNIndexDict"""
    book = Book("Книга", "Автор", 2025, "жанр")
    index = ISBNIndexDict()
    index.add(book)
    assert book.isbn in index.data
    assert book in index[book.isbn]
    index.remove(book)
    assert book.isbn not in index.data

def test_authorindex_multiple_books():
    """Тест добавления нескольких книг одного автора в AuthorIndexDict"""
    book1 = Book("Книга1", "Один Автор", 2025, "жанр")
    book2 = Book("Книга2", "Один Автор", 2026, "жанр")
    index = AuthorIndexDict()
    index.add(book1)
    index.add(book2)
    assert len(index["Один Автор"]) == 2
    index.remove(book1)
    assert len(index["Один Автор"]) == 1

def test_yearindex_operations():
    """Тест операций с YearIndexDict"""
    book1 = Book("Книга1", "Автор", 2025, "жанр")
    book2 = Book("Книга2", "Автор", 2025, "жанр")
    index = YearIndexDict()
    index.add(book1)
    index.add(book2)
    assert len(index[2025]) == 2
    index.remove(book1)
    assert len(index[2025]) == 1
    index.remove(book2)
    assert 2025 not in index.data

def test_genreindex_empty_removal():
    """Тест удаления жанра при отсутствии книг в GenreIndexDict"""
    book = Book("Книга", "Автор", 2025, "повесть")
    index = GenreIndexDict()
    index.add(book)
    assert "повесть" in index.data
    index.remove(book)
    assert "повесть" not in index.data

# тесты для класса Library
def test_library_add_book():
    """Тест добавления книги в библиотеку"""
    library = Library()
    book = Book("Книга", "Автор", 2025, "жанр")
    library.add_book(book)
    assert book in library
    assert len(library) == 1
    assert len(library.find_by_author("Автор")) == 1

def test_library_remove_book():
    """Тест удаления книги из библиотеки"""
    library = Library()
    book = Book("Книга", "Автор", 2025, "жанр")
    library.add_book(book)
    assert len(library) == 1
    library.remove_book(book)
    assert len(library) == 0
    assert len(library.find_by_author("Автор")) == 0

def test_library_find_by_author():
    """Тест поиска книг по автору"""
    library = Library()
    book1 = Book("Книга1", "Автор1", 2025, "жанр")
    book2 = Book("Книга2", "Автор2", 2024, "жанр")
    book3 = Book("Книга3", "Автор1", 2023, "жанр")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    result = library.find_by_author("Автор1")
    assert len(result) == 2
    assert book1 in result
    assert book3 in result

def test_library_find_by_genre():
    """Тест поиска книг по жанру"""
    library = Library()
    book1 = Book("Книга1", "Автор1", 2025, "повесть")
    book2 = Book("Книга2", "Автор2", 2024, "рассказ")
    book3 = Book("Книга3", "Автор3", 2023, "повесть")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    result = library.find_by_genre("повесть")
    assert len(result) == 2
    assert book1 in result
    assert book3 in result

def test_library_find_by_year():
    """Тест поиска книг по году"""
    library = Library()
    book1 = Book("Книга1", "Автор1", 2025, "жанр")
    book2 = Book("Книга2", "Автор2", 2021, "жанр")
    book3 = Book("Книга3", "Автор3", 2025, "жанр")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    result = library.find_by_year(2025)
    assert len(result) == 2
    assert book1 in result
    assert book3 in result

def test_library_find_by_isbn():
    """Тест поиска книги по ISBN"""
    library = Library()
    book = Book("Уникальная книга", "Автор", 2023, "жанр")
    library.add_book(book)
    result = library.find_by_isbn(book.isbn)
    assert len(result) == 1
    assert book in result

def test_library_duplicate_book():
    """Тест добавления дубликата книги в библиотеку"""
    library = Library()
    book = Book("Книга", "Автор", 2025, "жанр")
    library.add_book(book)
    library.add_book(book)
    assert len(library) == 2
    assert len(library.isbn_index) == 1