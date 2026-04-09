class Queue:
    @staticmethod
    def _to_format(pairs):
        if pairs is None:
            return dict()
        elif isinstance(pairs, dict):
            return dict(pairs)
        elif isinstance(pairs, (list, tuple)):
            return dict(pairs)
        else:
            return NotImplemented

    def __init__(self, pairs=None):
        self.pairs = self._to_format(pairs)

    def add(self, obj):
        key, value = obj
        if key in self.pairs:
            del self.pairs[key]
        self.pairs[key] = value

    def pop(self):
        if len(self.pairs) == 0:
            raise KeyError("Очередь пуста")
        for value in self.pairs.items():
            del self.pairs[value[0]]
            return value

    def __repr__(self):
        return f"Queue({list(self.pairs.items())})"

    def __len__(self):
        return len(self.pairs)


queue = Queue()

queue.add(("one", 1))
queue.add(("two", 2))
print(queue)
print()


queue = Queue([("one", 1)])

queue.add(("two", 2))
print(queue.pop())
print(queue.pop())
print(queue)
print()


queue = Queue({"one": 1, "two": 2})

print(len(queue))
queue.add(("three", 1))
print(len(queue))
print()


queue = Queue()

queue.add(("one", 1))
queue.add(("two", 2))
print(queue)
queue.add(("one", 10))
print(queue)
print()


queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)
