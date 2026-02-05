from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.year, self.month) == other
        elif isinstance(other, Month):
            return self.month == other.month and self.year == other.year
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, tuple):
            if self.year == other[0]:
                return self.month < other[1]
            elif self.year < other[0]:
                return True
            return False
        elif isinstance(other, Month):
            if self.year == other.year:
                return self.month < other.month
            elif self.year < other.year:
                return True
            return False
        return NotImplemented


print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))


months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))


months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))


print(Month(1999, 12) == (1999, 12))
print(Month(1999, 12) < (2000, 1))
print(Month(1999, 12) > (2000, 1))
print(Month(1999, 12) <= (1999, 12))
print(Month(1999, 12) >= (2000, 1))


month = Month(2023, 4)

print(month.__eq__(1))
print(month.__ne__(1.1))
print(month.__gt__(range(5)))
print(month.__lt__([1, 2, 3]))
print(month.__ge__({4, 5, 6}))
print(month.__le__({1: "one"}))
