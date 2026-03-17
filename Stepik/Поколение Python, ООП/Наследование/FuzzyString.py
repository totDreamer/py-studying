class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, str):
            return self.lower() != other.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, str):
            return len(self) < len(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, str):
            return len(self) > len(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, str):
            return len(self) <= len(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str):
            return len(self) >= len(other)
        return NotImplemented

    def __contains__(self, other):
        if isinstance(other, str):
            return other.lower() in self.lower()
        return NotImplemented


s1 = FuzzyString("BeeGeek")
s2 = FuzzyString("beegeek")

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)
print()


s = FuzzyString("BeeGeek")

print(s.__eq__(1))
print(s.__ne__(1.1))
print(s.__gt__(range(5)))
print(s.__lt__([1, 2, 3]))
print(s.__ge__({4, 5, 6}))
print(s.__le__({1: "one"}))
print()


s1 = FuzzyString("BeeGeek")
s2 = FuzzyString("bee")

print(s2 in s1)
print(s1 in s2)
