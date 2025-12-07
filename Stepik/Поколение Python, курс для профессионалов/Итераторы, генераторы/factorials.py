from itertools import accumulate

def factorials(n):
    yield from accumulate((num for num in range(1, n + 1)), lambda x, y: x * y)

numbers = factorials(6)
print(*numbers)

numbers = factorials(2)
print(next(numbers))
print(next(numbers))