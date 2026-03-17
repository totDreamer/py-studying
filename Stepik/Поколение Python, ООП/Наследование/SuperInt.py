class SuperInt(int):
    def repeat(self, n=2):
        if self < 0:
            return self.__class__(int("-" + str(self)[1:] * n))
        return self.__class__(int(str(self) * n))

    def to_bin(self):
        return f"{self:b}"

    def next(self):
        return self.__class__(self + 1)

    def prev(self):
        return self.__class__(self - 1)

    def __iter__(self):
        yield from map(
            lambda dig: self.__class__(dig), str(self) if self > 0 else str(self)[1:]
        )


superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))
print()


superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())
print()


superint = SuperInt(17)

print(superint.prev())
print(superint.next())
print()


superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)
