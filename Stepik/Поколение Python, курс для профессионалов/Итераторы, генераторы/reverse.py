def reverse(sequence):
    for a in reversed(sequence):
        yield a


print(*reverse([1, 2, 3, 4, 5]))

generator = reverse('beegeek')
print(type(generator))
print(*generator)