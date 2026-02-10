class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    @staticmethod
    def to_celsius(temperature):
        return (temperature - 32) * 5 / 9

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls(cls.to_celsius(temperature))

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


t = Temperature(5.5)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())


t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)

print(bool(t1))
print(bool(t2))
print(bool(t3))


t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())
