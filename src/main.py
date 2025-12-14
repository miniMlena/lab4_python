from src.library import Library
from src.random_generation import random_book

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    library = Library()

    for _ in range(10):
        book = random_book()
        library.add_book(book)
    library.add_book(book)

    print(library.book_collection)
    print()
    print(library.author_index)
    print()
    print(library.isbn_index)

if __name__ == "__main__":
    main()
