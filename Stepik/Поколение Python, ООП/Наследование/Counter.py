class Counter:
    def __init__(self, start=0):
        self._start = start
        self.value = self._start

    def inc(self, n=1):
        if not isinstance(n, int):
            raise TypeError("Должно быть передано целое число")
        self.value += n

    def dec(self, n=1):
        if not isinstance(n, int):
            raise TypeError("Должно быть передано целое число")
        if self.value - n < 0:
            self.value = 0
        else:
            self.value -= n


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self._limit = limit

    def inc(self, n=1):
        if not isinstance(n, int):
            raise TypeError("Должно быть передано целое число")
        if self.value + n > self._limit:
            self.value = self._limit
        else:
            self.value += n


print(issubclass(NonDecCounter, Counter))
print(issubclass(LimitedCounter, Counter))
print()


counter = Counter()

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)
print()


counter = NonDecCounter(10)

print(counter.value)
counter.inc()
counter.inc(10)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(50)
print(counter.value)
print()


counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
