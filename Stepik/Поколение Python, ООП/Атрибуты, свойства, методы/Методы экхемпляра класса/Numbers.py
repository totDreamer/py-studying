class Numbers:
    def __init__(self):
        self.collection = []

    def add_number(self, num):
        self.collection.append(num)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.collection))

    def get_odd(self):
        return list(filter(lambda x: x % 2 == 1, self.collection))


numbers = Numbers()

print(numbers.get_even())
print(numbers.get_odd())


numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())
