import random
from typing import Tuple
from src.constants import TITLES, AUTHORS, YEARS, GENRES
from src.book_class import Book

def random_book() -> Book:
    """
    Генерирует книгу со случайными параметрами
    
    :return: Случайно сгенерированная книга
    :rtype: Book
    """
    rand_title = random.choice(TITLES)
    rand_author = random.choice(AUTHORS)
    rand_year = random.choice(YEARS)
    rand_genre = random.choice(GENRES)

    return Book(rand_title, rand_author, rand_year, rand_genre)

def random_book_short() -> Tuple[str, str]:
    """
    Генерирует случайную комбинацию автора и названия
    
    :return: Случаное сочетание названия и автора
    :rtype: Tuple[str, str]
    """
    rand_title = random.choice(TITLES)
    rand_author = random.choice(AUTHORS)

    return (rand_title, rand_author)
