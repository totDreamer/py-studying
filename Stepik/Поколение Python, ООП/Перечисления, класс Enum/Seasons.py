from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, county_code):
        ru_names = ("зима", "весна", "лето", "осень")
        en_names = (seasone.name.lower() for seasone in self.__class__)
        values = dict(
            zip(self.__class__, ru_names if county_code == "ru" else en_names)
        )
        return values[self]


print(Seasons.FALL.text_value("ru"))
print(Seasons.FALL.text_value("en"))
