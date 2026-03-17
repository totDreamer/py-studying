class Summator:
    power = 1

    def total(self, n: int):
        return sum(map(lambda num: num**self.__class__.power, range(1, n + 1)))


class SquareSummator(Summator):
    power = 2


class QubeSummator(Summator):
    power = 3


class CustomSummator(Summator):
    def __init__(self, power):
        self.power = power

    def total(self, n: int):
        return sum(map(lambda num: num**self.power, range(1, n + 1)))


print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))
print()


summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27
print()


summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27
