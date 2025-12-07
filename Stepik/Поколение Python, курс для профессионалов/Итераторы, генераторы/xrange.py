class Xrange:
    def __init__(self, start, end, step = 1):
        self.start = start - step
        self.end = end - step
        self.step = step
        self.current = start - step
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step > 0:
            if self.current >= self.end:
                raise StopIteration
        else:
            if self.current <= self.end:
                raise StopIteration
        self.current += self.step
        return self.current

        
evens = Xrange(0, 10, 2)
print(*evens)

xrange = Xrange(0, 3, 0.5)
print(*xrange, sep='; ')