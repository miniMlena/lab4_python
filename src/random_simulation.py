import random
import time
from src.constants import AUTHORS, YEARS, GENRES
from src.book_class import Book
from src.book_collection import BookCollection
from src.library import Library
from src.random_books import random_book, random_book_short

def add_book(lib: Library) -> None:
    '''
    Добавление случайной книги

    :param lib: Библиотека, в которую добавится книга
    :return: Данная функция ничего не возвращает
    '''
    adding_book = random_book()
    lib.add_book(adding_book)
    print(f'Добавлена книга: {adding_book}')

def delete_book(lib: Library) -> None:
    '''
    Удаление случайной книги

    :param lib: Библиотека, из которой удалится книга
    :return: Данная функция ничего не возвращает
    '''
    book_for_del = random.choice(lib.book_collection)
    lib.remove_book(book_for_del)
    print(f'Удалена книга: {book_for_del}')

def search_by_author(lib: Library) -> None:
    '''
    Поиск книг случайного автора

    :param lib: Библиотека, в которой ищутся книги
    :return: Данная функция ничего не возвращает
    '''
    searching_author = random.choice(AUTHORS)
    found_by_author = lib.find_by_author(searching_author)
    print(f'Ищем книги автора {searching_author}...')
    print(found_by_author if found_by_author else 'Ничего не нашлось')

def search_by_genre(lib: Library) -> None:
    '''
    Поиск книг случайного жанра

    :param lib: Библиотека, в которой ищутся книги
    :return: Данная функция ничего не возвращает
    '''
    searching_genre = random.choice(GENRES)
    found_by_genre = lib.find_by_genre(searching_genre)
    print(f'Ищем книги жанра {searching_genre}...')
    print(found_by_genre if found_by_genre else 'Ничего не нашлось')
    
def search_by_year(lib: Library) -> None:
    '''
    Поиск книг случайного года выпуска

    :param lib: Библиотека, в которой ищутся книги
    :return: Данная функция ничего не возвращает
    '''
    searching_year = random.choice(YEARS)
    found_by_year = lib.find_by_year(searching_year)
    print(f'Ищем книги, вышедшие в {searching_year} году...')
    print(found_by_year if found_by_year else 'Ничего не нашлось')

def update_author_index(lib: Library) -> None:
    '''
    Изменение автора случайной книги

    :param lib: Рассматриваемая библиотека
    :return: Данная функция ничего не возвращает
    '''
    old_book = random.choice(lib.book_collection)
    print(f'Меняем автора книги {old_book}...')

    cur_author = AUTHORS.index(old_book.author)
    other_authors = AUTHORS[:cur_author]
    other_authors.extend(AUTHORS[cur_author + 1:])
    new_book = Book(old_book.title, random.choice(other_authors), old_book.year, old_book.genre)
    lib.remove_book(old_book)
    
    lib.add_book(new_book)
    print(f'Автор книги заменен на {new_book.author}')

def update_year_index(lib: Library) -> None:
    '''
    Изменение года выпуска случайной книги

    :param lib: Рассматриваемая библиотека
    :return: Данная функция ничего не возвращает
    '''
    old_book = random.choice(lib.book_collection)
    print(f'Меняем год выпуска книги {old_book}...')

    other_years = list(YEARS)
    other_years.remove(old_book.year)
    new_book = Book(old_book.title, old_book.author, random.choice(other_years), old_book.genre)
    lib.remove_book(old_book)
    
    lib.add_book(new_book)
    print(f'Год выпуска книги заменен на {new_book.year}')

def get_book_by_combo(lib: Library) -> None:
    '''
    Поиск книги по случайному сочетанию автора и названия

    :param lib: Рассматриваемая библиотека
    :return: Данная функция ничего не возвращает
    '''
    getting_book = random_book_short()
    getting_title = getting_book[0]
    getting_author = getting_book[1]
    print(f'Кто-то хочет взять такую книгу: {getting_author} - "{getting_title}"...')

    authors_books = lib.find_by_author(getting_author) # там все книги уникальные!
    suitable_books = BookCollection()
    for b in authors_books:
        if b.title == getting_title:
            suitable_books.add(b)
    if len(suitable_books) == 1:
        lib.remove_book(suitable_books[0])
        print('Кто-то получил свою книгу!')
    elif len(suitable_books) == 0:
        print('Такой книги нет в библиотеке')
    else:
        print(f'Несколько книг с такими параметрами:\n{suitable_books}\nНедостаточно сведений для получения.')

def get_book_by_isbn(lib: Library) -> None:
    '''
    Поиск книги по случайному ISBN

    :param lib: Рассматриваемая библиотека
    :return: Данная функция ничего не возвращает
    '''
    getting_isbn = random_book().isbn
    print(f'Кто-то хочет взять книгу с таким ISBN: {getting_isbn}...')

    suitable_book = lib.find_by_isbn(getting_isbn)
    if suitable_book:
        lib.remove_book(suitable_book[0])
        print('Кто-то получил свою книгу!')
    else:
        print('Такой книги нет в библиотеке')

events = (add_book, delete_book, search_by_author, search_by_genre, search_by_year, update_author_index, update_year_index, get_book_by_combo, get_book_by_isbn)

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Случайная симуляция работы с библиотекой

    :param steps: Количество шагов симуляции
    :type steps: int
    :param seed: seed для случайной генерации
    :type seed: int | None
    :return: Данная функция ничего не возвращает
    """
    if seed:
        random.seed(seed)
    
    library = Library()
    
    for i in range(10):
        rand_book = random_book()
        library.add_book(rand_book)

    print(f'\nНАЧАЛЬНЫЙ НАБОР КНИГ:\n{library}\n')

    for i in range(1, steps + 1):
        time.sleep(1)
        print(str(i) + ') ', end='')

        if not library:
            event = add_book
        else:
            event = random.choice(events)

        try:
            event(library)
        except Exception as e:
            print(f'Ошибка: {e}')
        print()

    time.sleep(1)
    print(f'КОНЕЧНЫЙ НАБОР КНИГ:\n{library if library else 'Ни одной книги не осталось! Все разобрали!'}')
