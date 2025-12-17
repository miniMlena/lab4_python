from typing import List
import re

TITLES: List = ['Мемуары', 'Вражда и дружба', 'Сэнсей и Мао Ито', 'Живые мозги', 'Мужчина в коробке', 'Пешком по Луне']
AUTHORS: List = ['Четкий Т.З.', 'Пухлый А.М.', 'Питонидзе Л.Р.', 'Восьмов М.И.', 'Моголь Г.М.']
YEARS: List = [1899, 1923, 1838, 1964, 1982, 2006, 2025]
GENRES: List = ['роман', 'повесть', 'рассказ']

EVENTS: List = ['add book', 'delete book', 'search by author', 'search by genre', 'search by year', 'update author index', 'get book by combo', 'get book by isbn']

INPUT_RE: re.Pattern = r"^\s*(?:steps=(\d+))?\s*(?:seed=(\d+))?\s*$"

'''text = 'steps=10seed=100'
match = re.search(INPUT_RE, text)
if match:
    print(match.group(1))
    print(match.group(2))
else:
    print('nichego')'''