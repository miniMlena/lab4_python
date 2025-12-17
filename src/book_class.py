from src.make_isbn import calculate_isbn

class Book:
    '''
    Docstring for Book
    '''
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = calculate_isbn(title, author, year, genre)

    def __repr__(self) -> str:
        return f'({self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn})'

    def __str__(self) -> str:
        return f'{self.author} - "{self.title}", {self.year}, {self.genre}, ISBN: {self.isbn}'