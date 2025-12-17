import random
from src.constants import TITLES, AUTHORS, YEARS, GENRES
from src.book_class import Book

def random_book():
    rand_title = random.choice(TITLES)
    rand_author = random.choice(AUTHORS)
    rand_year = random.choice(YEARS)
    rand_genre = random.choice(GENRES)

    return Book(rand_title, rand_author, rand_year, rand_genre)

def random_book_short():
    rand_title = random.choice(TITLES)
    rand_author = random.choice(AUTHORS)

    return (rand_title, rand_author)
