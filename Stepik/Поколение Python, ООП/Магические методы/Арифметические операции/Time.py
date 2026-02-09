class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        if isinstance(hours, int):
            self._hours = hours % 24

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        if isinstance(minutes, int):
            total = self._hours * 60 + minutes
            self._hours = (total // 60) % 24
            self._minutes = total % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(
                self.hours + other.hours, self.minutes + other.minutes
            )
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.hours += other.hours
            self.minutes += other.minutes
            return self
        return NotImplemented


time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)


time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)


time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)
