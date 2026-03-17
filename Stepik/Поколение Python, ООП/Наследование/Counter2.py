class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = start

    def inc(self, n=1):
        if not isinstance(n, int):
            raise TypeError("Должно быть передано целое число")
        self.value += n

    def dec(self, n=1):
        if not isinstance(n, int):
            raise TypeError("Должно быть передано целое число")
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, n=1):
        for _ in range(2):
            super().inc(n)

    def dec(self, n=1):
        for _ in range(2):
            super().dec(n)


print(issubclass(DoubledCounter, Counter))
print()


counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
print()


counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
