_sentinel = object()


class OrderedSet:
    def __init__(self, iterable=_sentinel):
        self._data = dict.fromkeys(iterable) if iterable is not _sentinel else {}

    def add(self, obj):
        self._data[obj] = None

    def discard(self, obj):
        self._data.pop(obj, None)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, obj):
        return obj in self._data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return list(self._data) == list(other._data)
        elif isinstance(other, set):
            return set(self._data) == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, OrderedSet):
            return list(self._data) != list(other._data)
        elif isinstance(other, set):
            return set(self._data) != other
        return NotImplemented


orderedset = OrderedSet(["bee", "python", "stepik", "bee", "geek", "python", "bee"])

print(*orderedset)
print(len(orderedset))
print()


orderedset = OrderedSet()

orderedset.add("green")
orderedset.add("green")
orderedset.add("blue")
orderedset.add("red")
print(*orderedset)
orderedset.discard("blue")
orderedset.discard("white")
print(*orderedset)
print()

print(OrderedSet(["green", "red", "blue"]) == OrderedSet(["green", "red", "blue"]))
print(OrderedSet(["green", "red", "blue"]) == OrderedSet(["red", "blue", "green"]))
print(OrderedSet(["green", "red", "blue"]) == {"blue", "red", "green"})
print(OrderedSet(["green", "red", "blue"]) == ["green", "red", "blue"])
print(OrderedSet(["green", "red", "blue"]) == 100)
