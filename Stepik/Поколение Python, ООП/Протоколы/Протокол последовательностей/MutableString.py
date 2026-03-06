class MutableString:
    def __init__(self, string=""):
        self._string = list(string)

    def lower(self):
        self._string = list(map(str.lower, self._string))

    def upper(self):
        self._string = list(map(str.upper, self._string))

    def __str__(self):
        return "".join(self._string)

    def __repr__(self):
        return f"MutableString('{''.join(self._string)}')"

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        yield from self._string

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__class__("".join(self._string[index]))
        elif isinstance(index, int):
            return self.__class__(self._string[index])
        raise IndexError("Неверно указан индекс или срез")

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self._string[index] = value
        elif isinstance(index, int):
            if len(value) == 1:
                self._string[index] = value
            else:
                self._string[index:] = value
        else:
            raise IndexError("Неверно указан индекс или срез")

    def __delitem__(self, index):
        if isinstance(index, slice):
            del self._string[index]
        elif isinstance(index, int):
            del self._string[index]
        else:
            raise IndexError("Неверно указан индекс")

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(str(self) + str(other))


mutablestring = MutableString("beegeek")

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))
print()


mutablestring = MutableString("Beegeek")

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
print()


mutablestring1 = MutableString("bee")
mutablestring2 = MutableString("geek")

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)
print()


mutablestring = MutableString("beegeek")

print(mutablestring)
mutablestring[0] = "B"
mutablestring[-4] = "G"
print(mutablestring)
print()

mutablestring = MutableString("beegeek")

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print()


mutablestring = MutableString("Ada Wong")
id1 = id(mutablestring)

mutablestring.upper()
id2 = id(mutablestring)

print(id1 == id2)
print()


mutablestring = MutableString("beegeek")

mutablestring[-1] = "ee"
print(mutablestring)

mutablestring[-2:] = "geek"
print(mutablestring)
print()


mutablestring = MutableString("beegeek")

del mutablestring[1:3]
print(mutablestring)
print()


mutablestring1 = MutableString("bee")
mutablestring2 = MutableString("geek")

concat = mutablestring1 + mutablestring2
slicing = mutablestring1[1:2]
plus_indexing = mutablestring2[1]
minus_indexing = mutablestring2[-1]

print(type(concat))
print(type(slicing))
print(type(plus_indexing))
print(type(minus_indexing))
