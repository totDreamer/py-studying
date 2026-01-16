from itertools import zip_longest


def intersperse(iterable, delimiter):
    it = zip_longest(iterable, "", fillvalue=delimiter)
    result = iter(list(num for tup in it for num in tup)[:-1])

    yield from result


print(*intersperse([1, 2, 3], 0))

inter = intersperse("beegeek", "!")
print(next(inter))
print(next(inter))
print(*inter)

print(*intersperse("A", "..."))

print(*intersperse("", "..."))

iterable = iter("Beegeek")
print(*intersperse(iterable, "+"))

print(*intersperse([], 100))
