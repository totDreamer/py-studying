from enum import Enum
from datetime import date, timedelta


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today: date, weekday: Weekday, considering_today: bool = False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today

    def days_until(self):
        today_weekday = self.today.weekday()
        target_weekday = self.weekday.value

        delta = (target_weekday - today_weekday) % 7

        if delta == 0 and not self.considering_today:
            delta = 7

        return delta

    def date(self):
        return self.today + timedelta(days=self.days_until())
