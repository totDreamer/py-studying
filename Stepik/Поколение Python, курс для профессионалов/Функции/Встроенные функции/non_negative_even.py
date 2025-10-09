def non_negative_even(numbers):
    return all(num >= 0 and num % 2 == 0 for num in numbers)

print(non_negative_even([0, 2, 4, 8, 16]))

print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))

print(non_negative_even([0, 0, 0, 0, 0]))