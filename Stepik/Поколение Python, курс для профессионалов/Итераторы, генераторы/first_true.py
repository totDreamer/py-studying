def first_true(iterable, predicate):
    result = list(filter(predicate, iterable))
    if result != []:
        return result[0]
    else:
        return None

numbers = [1, 1, 1, 1, 2, 4, 5, 6]
print(first_true(numbers, lambda num: num % 2 == 0))

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
print(first_true(numbers, lambda num: num > 10))