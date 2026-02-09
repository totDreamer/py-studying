class Queue:
    def __init__(self, *args):
        self.line = [arg for arg in args]

    def add(self, *args):
        self.line.extend(arg for arg in args)

    def pop(self):
        if self.line:
            elem = self.line[0]
            self.line = self.line[1:]
            return elem

    def __str__(self):
        return f"{' -> '.join(map(str, self.line))}"

    def __eq__(self, other):
        return self.line == other.line

    def __ne__(self, other):
        return self.line != other.line

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(*self.line + other.line)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.line += other.line
            return self
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.line):
                return self.__class__()
            return self.__class__(*self.line[: len(self.line) - other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.line):
                return self.__class__()
            return self.__class__(*self.line[other:])
        return NotImplemented


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)


queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)


queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)


queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)
