class PowerOf:
    def __init__(self, number):
        self.number = number
        self.topower = -1
    def __iter__(self):
        return self
    
    def __next__(self):
        self.topower += 1
        return self.number ** self.topower

power_of_two = PowerOf(2)
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))