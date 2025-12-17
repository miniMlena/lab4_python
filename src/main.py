import re
from src.constants import INPUT_RE
from src.random_generation import run_simulation

def main() -> None:
    """
    Точка входа в приложение
    :return: Данная функция ничего не возвращает
    """

    print('Добро пожаловать в случайную симуляцию работы с библиотекой!')
    print('Введите количество шагов и seed для симуляции в таком формате:')
    print('steps=steps_number seed=seed_number')
    print('Оба аргумента необязательны. Вы можете ввести оба аргумента, только число шагов, только seed или не вводить ничего! Число шагов по умолчанию равно 20. Для выхода введите exit или выход.')

    while ((user_input := input('Введите параметры или exit для выхода: ')) not in ('exit', 'выход')):

        users_steps, users_seed = None, None

        if user_input:
            if len(user_input.split()) > 2:
                print('Слишком много аргументов! Формат ввода: steps=steps_number seed=seed_number')
                continue
            match = re.search(INPUT_RE, user_input)
            if match:
                users_steps = match.group(1)
                users_seed = match.group(2)
            else:
                print('Некоректный ввод! Формат ввода: steps=steps_number seed=seed_number')
                continue
        
        users_steps = int(users_steps) if users_steps else None
        users_seed = int(users_seed) if users_seed else None
        
        if users_steps:        
            run_simulation(users_steps, users_seed)
        else:
            run_simulation(seed=users_seed)
    
if __name__ == "__main__":
    main()
