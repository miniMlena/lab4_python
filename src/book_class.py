class Book:
    '''
    Представляет книгу с метаданными и уникальным идентификатором
    
    Args:
        title: Название книги
        author: Автор книги
        year: Год публикации
        genre: Жанр книги
    
    Attributes:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год публикации
        genre (str): Жанр книги
        isbn (str): Международный стандартный книжный номер, вычисленный
            на основе метаданных книги
    '''
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = self.calculate_isbn(title, author, year, genre)

    def __repr__(self) -> str:
        """
        Создает строкове представление книги для отладки

        :return: Отладочное строковое представление пармаетров книги
        """
        return f'({self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn})'

    def __str__(self) -> str:
        """
        Создает строкове представление книги

        :return: Отформатированное строковое представление пармаетров книги
        """
        return f'{self.author} - "{self.title}", {self.year}, {self.genre}, ISBN: {self.isbn}'
    
    @staticmethod
    def calculate_isbn(title, author, year, genre) -> str:
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
        genre_code = (len(genre) * ord(genre[-1]) + ord(genre[0])) % 10

        isbn = f'978-{year_code}-{author_code:05d}-{title_code:03d}-{genre_code}'
        return isbn