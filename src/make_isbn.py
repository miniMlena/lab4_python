from src.constants import GENRES

def calculate_isbn(title, author, year, genre):
    """
    Генерация уникального ISBN исходя из параметров книги
    :param title: Название книги
    :param author: Автор книги
    :param year: Год выпуска книги
    :param genre: Жанр книги
    """
    year_code = year % 10
    author_code = (ord(author[0]) * ord(author[1]) * ord(author[2])) % 100_000
    title_code = (ord(title[0]) * ord(title[1])) % 1000
    genre_code = GENRES.index(genre)

    isbn = f'978-{year_code}-{author_code:05d}-{title_code:03d}-{genre_code}'
    return isbn

'''import random
title = random.choice(TITLES)
author = random.choice(AUTHORS)
year = random.choice(YEARS)
genre = random.choice(GENRES)

print(calculate_isbn(title, author, year, genre))'''