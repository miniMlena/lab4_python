# Лабораторная работа №5 — Отладка кодовой базы проекта на Python с помощью средств отладĸи
Моисеенко Милена Алексеевна, группа М8О-101БВ-25

## Цель
- заĸрепление навыĸов работы с отладчиĸом;
- формирование понимания типовых логичесĸих и runtime-ошибоĸ;
- освоение методиĸи поисĸа, анализа и устранения ошибоĸ;
- развитие умения объяснять причину неĸорреĸтного поведения программы. Логические и runtime-ошибки

## Ошибка 1 — Неверное логическое условие при проверке существования книги

### Место:
`library.py`, метод `remove_book`\
Внесенная ошибка:
    
    if book not in self.book_collection:\
        self.isbn_index.remove(book)\
        self.author_index.remove(book)\
        self.year_index.remove(book)\
        self.genre_index.remove(book)
        
    self.book_collection.remove(book)

### Симптом:
При удалении книги индексы не удаляются, что приводит к несогласованности данных. Можно удалить книгу из основной коллекции, но она останется в индексах.

### Как воспроизвести:
1. Запустить симуляцию с seed=42
2. На шаге 11 будет удалена книга жанра роман
3. На шаге 20 будут искаться книги жанра роман, там всё ещё будет эта книга
4. В итоговом списке книг в конце симуляции её не будет
5. Она будет найдена в индексах, но не в основной коллекции

### Отладка:
Установлен breakpoint на условие if. В отладчике видно, что выражение всегда будет False.\
Видно значение book, которое прояверяется:\
<img width="1042" height="200" alt="image" src="https://github.com/user-attachments/assets/d2b64b25-224d-4c72-bdbe-d844411bb872" />
И что эта книга ещё находится в book_collection на момент проверки:\
<img width="1041" height="379" alt="image" src="https://github.com/user-attachments/assets/fae501f2-5df6-402a-9bdd-b40968e9a0b4" />

### Причина:
Неправильный порядок операций: сначала проверяется, что книги нет в коллекции (что всегда False до удаления книги), а только потом она удаляется из `book_collection`. В итоге в индексах книга остается.

### Исправление:
Заменено на:

    self.book_collection.remove(book)
    
    if book not in self.book_collection:\
        self.isbn_index.remove(book)\
        self.author_index.remove(book)\
        self.year_index.remove(book)\
        self.genre_index.remove(book)

### Проверка:
После исправления индексы синхронизируются с основной коллекцией. Удаленные книги больше не находятся при поиске.

### Доказательства:
До:\
<img width="940" height="472" alt="image" src="https://github.com/user-attachments/assets/06d822fa-f0ea-4c77-a6bf-cadc1e99ab15" />

После исправления:\
<img width="942" height="379" alt="image" src="https://github.com/user-attachments/assets/0fd2e22a-a388-4563-b879-f41762063f07" />

В отладке тоже видно, что проверяемая книга уже не находится в book_collection:\
<img width="1115" height="319" alt="image" src="https://github.com/user-attachments/assets/9fa74d67-2a1f-4990-8df2-0bbad4203ea4" />


## Ошибка 2 — Неправильная обработка строки при вводе отрицательного числа шагов

### Место:
`parse_params.py`, функция `parse_simulation_parameters`\
Внесенная ошибка:

    if key == 'steps':
        try:
            steps_int = int(value)
            # Нет проверки, что steps_int - положительное число
            steps = steps_int
        except ValueError as e:
            raise ValueError(f"Ошибка в steps: {e}")

### Симптом:
При вводе steps=-10 программа не обрабатывает это корректно и не вызывается ошибка. Симуляция завершается, не выполнив ни одного шага, но выведя начальный и итоговый набор книг.

### Как воспроизвести:
1. Запустите симуляцию с steps=-10
2. Сразу после вывода начального списка книг не будет выполнено ни одного шага симуляции и выведется итоговый список книг

### Отладка:
Брейкпоинт на цикл со steps в random_simulation.py
Видим, что steps действительно равно -10, а в блоке кода до этого генерировался стартовый набор случайных книг.
<img width="1189" height="182" alt="image" src="https://github.com/user-attachments/assets/0a4d7694-6786-4e85-9674-9a117165b632" />

### Причина:
Отсутствует проверка на положительное значение steps перед запуском симуляции

### Исправление:
Заменено на:

    if key == 'steps':
        try:
            steps_int = int(value)
            if steps_int <= 0:
                raise ValueError("steps должен быть положительным числом")
            steps = steps_int```\
        except ValueError as e:
            raise ValueError(f"Ошибка в steps: {e}")

### Проверка:
Теперь выводится ошибка "steps должен быть положительным числом" и симуляция не запускается.

### Доказательства:
До:\
<img width="693" height="572" alt="image" src="https://github.com/user-attachments/assets/98f033b1-9cd5-4edb-acca-1a788ab37ebf" />

После исправления:\
<img width="504" height="66" alt="image" src="https://github.com/user-attachments/assets/9d93043e-6144-4a03-aae0-183a1f40eb60" />

В отладке тоже видно значение int_steps и выбрасываемую ошибку:\
<img width="936" height="317" alt="image" src="https://github.com/user-attachments/assets/5b4c5b6c-927c-4aab-aa48-bae03abce248" />

## Ошибка 3 — Ошибка границы цикла (Off-by-One)

### Место:
`random_simulation.py`, функция `run_simulation`\
Внесенная ошибка:\
```for i in range(1, steps):```

### Симптом:
Выполняется на 1 меньше шагов, чем указывает пользователь.

### Как воспроизвести:
1. Запустите симуляцию с steps=5, seed=1
2. Вывод показывает 4 шага вместо 5.

### Отладка:
Брейкпоинт на for i in range(1, steps): и выводе конечного набора книг
Видим, что на момент вывода конечного набора книг i=4:\
<img width="1125" height="438" alt="image" src="https://github.com/user-attachments/assets/60dba579-85a4-4adf-8a6a-ee77a38212cc" />
То есть последний шаг номер 4.

### Причина:
Неправильный параметр в функции `range()`: используется `range(1, steps)` вместо `range(1, steps + 1)`.

### Исправление:
Заменено на:\
```for i in range(1, steps + 1):```

### Проверка:
После исправления выполняется именно столько шагов, сколько указано.

### Доказательства:
До (последний шаг - 4):\
<img width="682" height="387" alt="image" src="https://github.com/user-attachments/assets/93c63ee4-b33d-4033-b4e9-5a745835e468" />

После (последний шаг - 5):\
<img width="675" height="397" alt="image" src="https://github.com/user-attachments/assets/eba3f60e-3fce-4395-8324-36822d323beb" />

В отладчике также видно, что значение i на момент вывода конечного набора книг теперь равно 5:\
<img width="1112" height="418" alt="image" src="https://github.com/user-attachments/assets/f39769af-832b-47cb-80c9-d42573afaf4e" />


## Ошибка 4 — Неправильное сравнение

### Место:
`random_simulation.py`, функция `run_simulation`\
Внесенная ошибка:

    if seed:
        random.seed(seed)

### Симптом:
Условие `if seed:` не срабатывает при `seed=0`, так как используется оператор сравнения идентичности `is`, а не проверка значения.

Как воспроизвести:\
1. Запустите симуляцию с steps=5 seed=0
2. Снова запустите симуляцию с steps=5 seed=0
3. Результат окажется разным, несмотря на заданный сид

### Отладка:
Брейкпоинт на random.seed(seed). Видно, что программа ни разу не остановилась на брейкпоинте, значит она не доходит до него, т.е. условие if не выполняется.

### Причина:
Использование условия `if seed:` вместо проверки `if seed is not None:` для проверки наличия параметра. Значение 0 считается "ложным".

### Исправление:
Заменено на:

    if seed is not None:
        random.seed(seed)

### Проверка:
Дважды запустим симуляцию с steps=5 seed=0. Теперь рузельтаты идентичны.

### Доказательства:
До:\
Первый запуск:\
<img width="955" height="486" alt="image" src="https://github.com/user-attachments/assets/398dfcd1-b6f6-49f8-a41e-28ef172565da" />

Второй запуск:\
<img width="793" height="471" alt="image" src="https://github.com/user-attachments/assets/3610511b-9153-47c5-bf60-c458fc56b759" />

Случайная генерация разная.

После:\
Первый запуск:\
<img width="951" height="509" alt="image" src="https://github.com/user-attachments/assets/e4099b7a-0c7b-4eb9-92b2-db2919a3b5f2" />

Второй запуск:\
<img width="944" height="510" alt="image" src="https://github.com/user-attachments/assets/88a59512-f8d3-4669-9260-b55e40592dc4" />
Идентичная генерация.

В отладчике видно, что условие if выполнилось и была выполнена команда ```random.seed(seed)```
<img width="529" height="116" alt="image" src="https://github.com/user-attachments/assets/bddf418b-6c3e-4a2a-8e34-5cbf7112ea7c" />


## Ошибка 5 — Перепутаны параметры объекта

### Место:
`random_simulation.py`, функция `get_book_by_combo`\
Внесенная ошибка:\
```if b.author == getting_title:```

### Симптом:
Читатель не получает книгу по комбинации названия и автора, даже когда подходящая книга есть в библиотеке.

Как воспроизвести:\
1. Запустите симуляцию с seed=177.
2. На шаге 13 и 18 в библиотеке есть запрашиваемые книги, но выбрасывается "Такой книги нет в библиотеке".

### Отладка:
Брейкпоинт на if и print логов.
Видим, что suitable_books пустой:\
<img width="1102" height="252" alt="image" src="https://github.com/user-attachments/assets/e752ada0-77a1-42b2-b691-5997f452608b" />

Хотя рассматриваемая книга подходит по искомым параметрам:\
<img width="1110" height="251" alt="image" src="https://github.com/user-attachments/assets/6ce2a962-5e78-42c7-95cd-6a759b44c776" />

### Причина:
Перепутаны параметры title и author.

### Исправление:
Заменено на:\
```if b.title == getting_title:```

### Проверка:
Запустим симуляцию с теми же параметрами и теперь читатель получит свою книгу.

### Доказательства:
До:\
<img width="880" height="316" alt="image" src="https://github.com/user-attachments/assets/fea785e1-02ab-45c5-9e30-603319f7c894" />

После:\
<img width="885" height="325" alt="image" src="https://github.com/user-attachments/assets/60f9ca52-676b-4c73-972c-d8e5d65af1f7" />

В отладке видим, что книга с нужными параметрами теперь добавляется в suitable_books:\
<img width="1292" height="124" alt="image" src="https://github.com/user-attachments/assets/a61598d2-b0da-47e4-8789-b025d5a6bb5e" />


## Ошибка 6 — Сравнение через is вместо ==

### Место:
`parse_params.py`, функция `parse_simulation_parameters`\
Внесенная ошибка:\
```if key is 'steps':```

### Симптом:
Программа не считывает параметр steps из ввода и всегда выдает ошибку "Неизвестный параметр: 'steps'. Доступно: steps, seed".

### Как воспроизвести:
1. Запустите симуляцию с steps=10 seed=76
2. В консоли увидите ошибку "Неизвестный параметр: 'steps'. Доступно: steps, seed"

### Отладка:
Брейкпоинт на if и в отладчике видим, что команды внутри if не выполнялись и программа сразу выбросила исключение:\
<img width="1056" height="593" alt="image" src="https://github.com/user-attachments/assets/156661bd-ba3f-40ef-94de-958a63056f4a" />

### Причина:
Оператор is сравнивает не по значению, а по адресу в памяти.

### Исправление:
Заменено на:\
```if key == 'steps':```

### Проверка:
Теперь программа корректно считывает параметр steps из ввода.

### Доказательства:
До:\
<img width="485" height="69" alt="image" src="https://github.com/user-attachments/assets/a158c651-5b2f-4783-b7bb-6f948d49ae32" />

После:\
<img width="683" height="170" alt="image" src="https://github.com/user-attachments/assets/2f699fac-c7b2-4fe7-a03d-5d22b8482b96" />

В отладке видим, что код внутри if теперь исполняется:\
<img width="1048" height="466" alt="image" src="https://github.com/user-attachments/assets/dfd80bab-c6aa-406d-b200-e064160a6399" />

## Чему я научилась
- работа с отладчиĸом
- методиĸа поисĸа, анализа и устранения ошибоĸ

