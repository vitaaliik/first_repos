import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or quantity > (max - min + 1):
        print("Некоректні дані. Будь ласка, перевірте вхідні параметри.")
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    sorted_numbers = sorted(numbers)
    return sorted_numbers

lottery_numbers = get_numbers_ticket(4, 50, 6)
if lottery_numbers:
    print("Ваші лотерейні числа:", lottery_numbers)
