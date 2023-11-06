def average(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = average(numbers)

if result is not None:
    print(f"Среднее арифметическое: {result}")
else:
    print("putoi cod")

import statistics

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = statistics.mean(numbers)

print(f"Среднее арифметическое: {result}")
