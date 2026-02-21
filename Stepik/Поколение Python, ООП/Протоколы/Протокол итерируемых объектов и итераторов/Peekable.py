_sentinel = object()


class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.has_buffer = False
        self.buffer = None

    def peek(self, default=_sentinel):
        if not self.has_buffer:
            try:
                self.buffer = next(self.iterable)
                self.has_buffer = True
            except StopIteration:
                if default is _sentinel:
                    raise StopIteration
                return default
        return self.buffer

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_buffer:
            self.has_buffer = False
            return self.buffer
        return next(self.iterable)


iterator = Peekable("beegeek")

print(next(iterator))
print(next(iterator))
print(*iterator)


iterator = Peekable("Python")

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())
