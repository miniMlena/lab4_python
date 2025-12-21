from typing import Tuple

def parse_simulation_parameters(user_input: str) -> Tuple[int, int]:
    """
    Извлекает параметры steps и seed из строки

    :param user_input: Входная строка пользователя
    :returns: Значения steps и seed
    """
    steps = 20
    seed = None

    parts = user_input.split()
    
    for part in parts:
        if '=' not in part:
            raise ValueError("Некоректный ввод! Формат ввода: steps=steps_number seed=seed_number")
        
        key, value = part.split('=', 1)
        
        if key == 'steps':
            try:
                steps_int = int(value)
                if steps_int <= 0:
                    raise ValueError("steps должен быть положительным числом")
                steps = steps_int
            except ValueError as e:
                raise ValueError(f"Ошибка в steps: {e}")
            
        elif key == 'seed':
            try:
                seed = int(value)
            except ValueError:
                raise ValueError(f"seed должен быть целым числом: '{value}'")
                
        else:
            raise ValueError(f"Неизвестный параметр: '{key}'. Доступно: steps, seed")
    
    return steps, seed