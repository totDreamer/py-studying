from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=None):
        self.iterable = iterable if iterable is not None else []

    def add(self, num: (int, float)):
        self.iterable.append(num)

    def clear(self):
        self.iterable = []

    @abstractmethod
    def result(self):
        raise NotImplementedError


class MinStat(Stat):
    def result(self):
        if not self.iterable:
            return None
        return min(self.iterable)


class MaxStat(Stat):
    def result(self):
        if not self.iterable:
            return None
        return max(self.iterable)


class AverageStat(Stat):
    def result(self):
        if not self.iterable:
            return None
        return sum(self.iterable) / len(self.iterable)


minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
print()


minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

for i in range(1, 6):
    minstat.add(i)
    maxstat.add(i)
    averagestat.add(i)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
print()


minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
