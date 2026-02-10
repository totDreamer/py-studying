from functools import total_ordering


@total_ordering
class RomanNumeral:
    VALUES = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, num):
        if isinstance(num, str):
            self._number = self.__class__.to_arabic(num)
        elif isinstance(num, int):
            self._number = num
        else:
            raise TypeError("Неподдерживаемый тип данных")

    def __str__(self):
        return f"{self.__class__.to_roman(self.number)}"

    @classmethod
    def to_roman(cls, number):
        if isinstance(number, int):
            result = ""
            for value, symbol in cls.VALUES:
                while number >= value:
                    result += symbol
                    number -= value
            return result
        return NotImplemented

    @classmethod
    def to_arabic(cls, number):
        if isinstance(number, str):
            romanian_dict = {value: key for key, value in cls.VALUES if len(value) == 1}
            result = 0
            for num in range(len(number) - 1):
                if romanian_dict[number[num]] < romanian_dict[number[num + 1]]:
                    result -= romanian_dict[number[num]]
                else:
                    result += romanian_dict[number[num]]
            result += romanian_dict[number[-1]]
            return result
        return NotImplemented

    def __int__(self):
        return self.number

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.number + other.number)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.number - other.number)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.number < other.number
        return NotImplemented


number = RomanNumeral("IV") + RomanNumeral("VIII")

print(number)
print(int(number))


number = RomanNumeral("X") - RomanNumeral("VI")

print(number)
print(int(number))


a = RomanNumeral("X")
b = RomanNumeral("XII")

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
