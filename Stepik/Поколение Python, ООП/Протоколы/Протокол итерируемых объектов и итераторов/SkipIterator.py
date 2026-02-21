class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterable)
        for _ in range(self.n):
            next(self.iterable, value)
        return value


skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1
)  # пропускаем по одному элементу

print(*skipiterator)

skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2
)  # пропускаем по два элемента

print(*skipiterator)


skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0
)  # не пропускаем элементы

print(*skipiterator)
