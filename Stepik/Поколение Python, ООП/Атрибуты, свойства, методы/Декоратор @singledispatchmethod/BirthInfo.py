from functools import singledispatchmethod
from datetime import date


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_iso(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except (TypeError, ValueError):
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(tuple)
    @__init__.register(list)
    def _from_list_tuple(self, birth_date):
        try:
            self.birth_date = date(*birth_date)
        except (TypeError, ValueError):
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        this_year_birthday = date(
            today.year, self.birth_date.month, self.birth_date.day
        )
        years = today.year - self.birth_date.year
        if today < this_year_birthday:
            return years - 1
        else:
            return years


birthinfo1 = BirthInfo("2020-09-18")
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)


birthday = date(1999, 11, 7)
today = date.today()
birthinfo = BirthInfo(birthday)

print(birthinfo.age)
print(birthinfo.age == 26)
