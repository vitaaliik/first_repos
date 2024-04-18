import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000):
        return []
    
    numbers= set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    sorted_numbers = sorted(numbers)
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
