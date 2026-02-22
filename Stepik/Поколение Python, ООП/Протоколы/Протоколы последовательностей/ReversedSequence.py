class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        yield from reversed(self.sequence)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")
        if key < 0 or key > len(self.sequence):
            raise IndexError("Неверный индекс")
        return self.sequence[::-1][key]


reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])


numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])


numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))
