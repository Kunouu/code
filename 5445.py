def average(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return None

numbers = [1, 2, 3, 4, 5]
result = average(numbers)

if result is not None:
    print(f"Среднее арифметическое: {result}")
else:
    print("Список пуст")

import statistics

numbers = [1, 2, 3, 4, 5]
result = statistics.mean(numbers)

print(f"Среднее арифметическое: {result}")
