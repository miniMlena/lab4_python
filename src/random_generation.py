import random
from src.constants import TITLES, AUTHORS, YEARS, GENRES, EVENTS
from src.book_class import Book
from src.library import Library

def random_book():
    rand_title = random.choice(TITLES)
    rand_author = random.choice(AUTHORS)
    rand_year = random.choice(YEARS)
    rand_genre = random.choice(GENRES)

    return Book(rand_title, rand_author, rand_year, rand_genre)

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed:
        random.seed(seed)
    
    lib = Library()
    
    for i in range(10):
        book = random_book()
        lib.add_book(book)

    for _ in range(steps):
        event = random.choice(EVENTS)
        