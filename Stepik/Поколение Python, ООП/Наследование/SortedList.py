from collections.abc import MutableSequence
import bisect


class SortedList(MutableSequence):
    def __init__(self, iterable=None):
        self._data = sorted(iterable) if iterable is not None else []

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, index):
        del self._data[index]

    def __setitem__(self, index, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def __repr__(self):
        return f"SortedList({self._data})"

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def append(self, value):
        raise NotImplementedError

    def extend(self, iterable):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def add(self, value):
        bisect.insort(self._data, value)

    def discard(self, value):
        self._data = [x for x in self._data if x != value]

    def update(self, iterable):
        for item in iterable:
            bisect.insort(self._data, item)

    def __add__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        return SortedList(self._data + other._data)

    def __iadd__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        self.update(other._data)
        return self

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return SortedList(self._data * n)

    def __imul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        self._data *= n
        self._data.sort()
        return self


numbers = SortedList([5, 3, 4, 2, 1])


print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)
print()


numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)
print()


numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)
