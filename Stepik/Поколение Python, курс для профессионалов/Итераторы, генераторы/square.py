class Square:
    def __init__(self, n):
        self.start = 0
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start == self.n:
            raise StopIteration
        self.start += 1
        return self.start**2

squares = Square(2)
print(next(squares))
print(next(squares))


squares = Square(10)
print(list(squares))


squares = Square(1)
print(list(squares))