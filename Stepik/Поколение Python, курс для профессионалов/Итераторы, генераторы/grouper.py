from itertools import zip_longest

def grouper(iterable, n):
    it = ([iter(iterable)] * n)
    yield from zip_longest(*it)


numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))