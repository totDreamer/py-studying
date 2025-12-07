def first_largest(iterable, number):
    with_index = enumerate(iterable, 0)
    for num in with_index:
        if num[1] > number:
            return num[0]
    return -1

numbers = [10, 2, 14, 7, 7, 18, 20]
print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])
print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))