from src.parse_params import parse_simulation_parameters
from src.random_simulation import run_simulation

def main() -> None:
    """
    Точка входа в приложение

    :return: Данная функция ничего не возвращает
    """

    print('Добро пожаловать в случайную симуляцию работы с библиотекой!')
    print('Введите количество шагов и seed для симуляции в таком формате (и именно в таком порядке):')
    print('steps=steps_number seed=seed_number')
    print('Оба аргумента необязательны. Вы можете ввести оба аргумента, только число шагов, только seed или не вводить ничего! Число шагов по умолчанию равно 20. Для выхода введите exit или выход.')

    while ((user_input := input('Введите параметры или exit для выхода: ').strip()) not in ('exit', 'выход')):

        try:
            users_steps, users_seed = parse_simulation_parameters(user_input)
        except Exception as e:
            print(e)
            continue

        if users_steps:        
            run_simulation(users_steps, users_seed)
        else:
            run_simulation(seed=users_seed)
    
if __name__ == "__main__":
    main()
