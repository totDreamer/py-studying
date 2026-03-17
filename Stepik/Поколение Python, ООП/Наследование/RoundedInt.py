class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            num = num + num % 2
        else:
            num = num + (1 - num % 2)
        instance = super().__new__(cls, num)
        return instance


print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))
print()


roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
