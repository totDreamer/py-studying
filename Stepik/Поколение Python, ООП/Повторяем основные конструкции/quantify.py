def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return len(list(filter(predicate, iterable)))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x > 1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x % 2 == 0))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x < 0))
