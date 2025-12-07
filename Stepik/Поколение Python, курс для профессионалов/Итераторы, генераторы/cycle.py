class Cycle:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.reserve = iterable
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterable)
        except StopIteration:
            self.iterable = iter(self.reserve)
            return next(self.iterable)


cycle = Cycle('be')
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))


cycle = Cycle([1])
print(next(cycle) + next(cycle) + next(cycle))


cycle = Cycle(range(100_000_000))
print(next(cycle))
print(next(cycle))