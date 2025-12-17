import random
import time
from src.constants import TITLES, AUTHORS, YEARS, GENRES, EVENTS
from src.book_class import Book
from src.book_collection import BookCollection
from src.library import Library
from src.random_books import random_book, random_book_short

def add_book(lib):
    adding_book = random_book()
    lib.add_book(adding_book)
    print(f'Добавлена книга: {adding_book}')

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed:
        random.seed(seed)
    
    lib = Library()
    
    for i in range(10):
        rand_book = random_book()
        lib.add_book(rand_book)

    print(f'\nНАЧАЛЬНЫЙ НАБОР КНИГ:\n{lib}\n')

    for i in range(1, steps + 1):
        time.sleep(1)
        print(str(i) + ') ', end='')
        event = random.choice(EVENTS)

        #!!!!
        print(event)

        if event == 'add book':
            adding_book = random_book()
            lib.add_book(adding_book)
            print(f'Добавлена книга: {adding_book}')

        elif event == 'delete book':
            if not lib.book_collection:
                print('Нет книг для удаления')
            book_for_del = random.choice(lib.book_collection)
            lib.remove_book(book_for_del)
            print(f'Удалена книга: {book_for_del}')

        elif event == 'search by author':
            searching_author = random.choice(AUTHORS)
            found_by_author = lib.find_by_author(searching_author)
            print(f'Ищем книги автора {searching_author}...')
            print(found_by_author if found_by_author else 'Ничего не нашлось')

        elif event == 'search by genre':
            searching_genre = random.choice(GENRES)
            found_by_genre = lib.find_by_genre(searching_genre)
            print(f'Ищем книги жанра {searching_genre}...')
            print(found_by_genre if found_by_genre else 'Ничего не нашлось')

        elif event == 'search by year':
            searching_year = random.choice(YEARS)
            found_by_year = lib.find_by_year(searching_year)
            print(f'Ищем книги, вышедшие в {searching_year} году...')
            print(found_by_year if found_by_year else 'Ничего не нашлось')

        elif event == 'update author index':
            old_book = random.choice(lib.book_collection)
            print(f'Меняем автора книги {old_book}...')

            cur_author = AUTHORS.index(old_book.author)
            other_authors = AUTHORS[:cur_author]
            other_authors.extend(AUTHORS[cur_author + 1:])
            new_book = Book(old_book.title, random.choice(other_authors), old_book.year, old_book.genre)
            lib.remove_book(old_book)
            
            lib.add_book(new_book)
            print(f'Автор книги заменен на {new_book.author}')

        # Добавляются одинаковые книги в дикты!! И isbn не меняется при update index (просто добавить это в new_book)!!

        elif event == 'get book by combo':
            getting_book = random_book_short()
            getting_title = getting_book[0]
            getting_author = getting_book[1]
            print(f'Кто-то хочет взять эту книгу: {getting_author} - "{getting_title}"...')
            try:
                authors_books = lib.find_by_author(getting_author)
                suitable_books = BookCollection()
                for b in authors_books:
                    if b.title == getting_title:
                        suitable_books.add(b)
                if len(suitable_books) == 1:
                    lib.remove_book(suitable_books[0])
                    print('Кто-то получил свою книгу!')
                elif len(suitable_books) == 0:
                    raise ValueError('Нет книги с такими параметрами')
                else:
                    print(f'Несколько книг с такими параметрами:\n{suitable_books}\nВоспользуйтесь получением через ISBN.')
            except Exception as e:
                print(f'Ошибка: {e}')

        elif event == 'get book by isbn':
            getting_isbn = random_book().isbn
            print(f'Кто-то хочет взять книгу с таким ISBN: {getting_isbn}...')
            try:
                suitable_book = lib.find_by_isbn(getting_isbn)
                if suitable_book:
                    lib.remove_book(suitable_book[0])
                    print('Кто-то получил свою книгу!')
                else:
                    raise ValueError('Такой книги нет в библиотеке')
            except Exception as e:
                print(f'Ошибка: {e}')

        print()

    print('КОНЕЧНЫЙ НАБОР КНИГ:')
    print(lib)

