from datetime import date
from abc import ABC, abstractmethod


class CountriesDate(ABC):
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    @abstractmethod
    def format(self):
        raise NotImplementedError

    def iso_format(self):
        return self.date.strftime("%Y-%m-%d")


class USADate(CountriesDate):
    def format(self):
        return self.date.strftime("%m-%d-%Y")


class ItalianDate(CountriesDate):
    def format(self):
        return self.date.strftime("%d/%m/%Y")


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())
print()


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())
