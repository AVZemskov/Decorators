import os
from datetime import datetime



def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)

        log_entry = (
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Function: {old_function.__name__} | "
            f"Args: {args}, Kwargs: {kwargs} | "
            f"Result: {result}\n"
        )

        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(log_entry)

        return result
    return new_function

@logger
def generate_prims(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5)):
            if num % 1 == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
    return primes

@logger
def transform_data(data, multiplier=1):
    processed = (x * multiplier for x in data if x > 0)
    return  list(processed)

@logger
def calculate_stats(numbers):
    it = iter(numbers)
    total = sum(it)
    count = len(numbers)
    average = total / count if count else 0
    return {"sum": total, "avg": round(average, 2)}


if __name__ == "__main__":

    if os.path.exists('main.log'):
        os.remove('main.log')

    primes = generate_prims(15)
    print(f"Простые числа до 15: {primes}")

    transformed = transform_data([-2, 0, 5, 10, -3], multiplier=3)
    print(f"Трансформированные данные: {transformed}")

    stats = calculate_stats([10, 20, 30, 40])
    print(f"Статистика: {stats}")

    print("\nСодержимое файла main.log:")
    with open('main.log', 'r', encoding='utf-8') as f:
        print(f.read())