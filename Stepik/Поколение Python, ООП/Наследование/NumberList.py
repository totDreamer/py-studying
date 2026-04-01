from collections import UserList


class NumberList(UserList):
    @staticmethod
    def is_valid(iterable):
        try:
            iterable = list(iterable)
        except TypeError:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

        if not all(isinstance(x, (int, float)) for x in iterable):
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

        return iterable

    def __init__(self, iterable=()):
        super().__init__(self.is_valid(iterable))

    def __add__(self, other):
        other = self.is_valid(other)
        return self.__class__(self.data + other)

    def __radd__(self, other):
        other = self.is_valid(other)
        return self.__class__(other + self.data)

    def __iadd__(self, other):
        other = self.is_valid(other)
        self.data += other
        return self

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            value = self.is_valid(value)
        elif not isinstance(value, (int, float)):
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

        self.data[index] = value

    def append(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
        self.data.append(value)

    def extend(self, value):
        value = self.is_valid(value)
        self.data.extend(value)

    def insert(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
        self.data.insert(index, value)
