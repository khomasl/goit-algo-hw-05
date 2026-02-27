import re
from typing import Callable

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def generator_numbers(text: str):
    # Список всіх слів з тексту, крім першого і останнього
    words = text.strip().split(' ')[1:-1]
    # _, *words, _ = text.strip().split(' ')

    for word in words:
        # # Перевірка, чи після числа одразу не йде символ пунктуації 
        # if not word[-1:].isdigit():
        #     continue

        if is_float(word):
            yield float(word)

# з regexp            
def generator_numbers(text: str):
    pattern = r" \d+\.?\d+ "
    numbers = re.findall(pattern, text)
    print(numbers)
    for number in numbers:
        yield float(number)
        
def sum_profit(text: str, generator_numbers: Callable):
    total = 0
    for number in generator_numbers(text):
        total += number
    
    return total

text = """
        1. Загальний дохід працівника складається з декількох частин: 
        1000.01 як основний дохід 2, 1.2.3 як
        доповнений додатковими надходженнями 27.45 і 324.00 доларів 1.3.
    """
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
