def count_iterable(iterable):
    return sum(1 for _ in iter(iterable))

print(count_iterable([1, 2, 3, 4, 5]))

numbers = iter([1, 2, 3, 4, 5, 6, 7])
print(count_iterable(numbers))

data = tuple(range(432, 3845, 17))
print(count_iterable(data))