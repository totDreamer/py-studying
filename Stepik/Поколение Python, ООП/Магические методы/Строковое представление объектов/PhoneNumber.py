from re import search


class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = search(r"(\d{3})\s?(\d{3})\s?(\d{4})", phone_number)

    def __str__(self):
        return f"({self.phone_number.group(1)}) {self.phone_number.group(2)}-{self.phone_number.group(3)}"

    def __repr__(self):
        return f"PhoneNumber('{''.join(self.phone_number.groups())}')"


phone = PhoneNumber("9173963385")

print(str(phone))
print(repr(phone))


phone = PhoneNumber("918 396 3389")

print(str(phone))
print(repr(phone))


phone1 = PhoneNumber("9173963385")
phone2 = PhoneNumber("918 396 3389")
phone3 = PhoneNumber("919 333 3344")

print(phone1, phone2, phone3, sep=", ")
print([phone1, phone2, phone3])
print(phone1.phone_number)
