from src.book_class import Book
from src.book_collection import BookCollection
from src.index_dict import ISBNIndexDict, AuthorIndexDict, YearIndexDict, GenreIndexDict

class Library:

    def __init__(self):
        self.book_collection = BookCollection()

        self.isbn_index = ISBNIndexDict()
        self.author_index = AuthorIndexDict()
        self.year_index = YearIndexDict()
        self.genre_index = GenreIndexDict()

    def __len__(self):
        return self.book_collection.__len__()
    
    def __iter__(self):
        return self.book_collection.__iter__()

    def __str__(self):
        return self.book_collection.__str__()

    def add_book(self, book: Book):
        """
        Добавление книги в библиотеку
        :param book: Добавляемая книга
        """
        if book not in self.book_collection:
            self.isbn_index.add(book)
            self.author_index.add(book)
            self.year_index.add(book)
            self.genre_index.add(book)

        self.book_collection.add(book)

    def remove_book(self, book: Book):
        """
        Удаление книги из библиотеки
        :param book: Удаляемая книга
        """
        self.book_collection.remove(book)
        
        if book not in self.book_collection:
            self.isbn_index.remove(book)
            self.author_index.remove(book)
            self.year_index.remove(book)
            self.genre_index.remove(book)

    def find_by_author(self, author: str) -> BookCollection:
        return self.author_index[author]
        '''if res:
            output = [book.__str__() + '\n' for book in res]
            return output
        else:
            return '''
        
    def find_by_genre(self, genre: str) -> BookCollection:
        return self.genre_index[genre]
    
    def find_by_year(self, year: int) -> BookCollection:
        return self.year_index[year]
    
    def find_by_isbn(self, isbn: str) -> BookCollection:
        return self.isbn_index[isbn]