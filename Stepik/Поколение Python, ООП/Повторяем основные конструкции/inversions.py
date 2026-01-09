from itertools import combinations


def inversions(sequence):
    return len(list(filter(lambda x: x[0] > x[1], combinations(sequence, 2))))


sequence = [3, 1, 4, 2]
print(inversions(sequence))

sequence = [1, 2, 3, 4, 5]
print(inversions(sequence))

sequence = [4, 3, 2, 1]
print(inversions(sequence))

sequence = [1, 1, 1, 1, 1, 1]
print(inversions(sequence))
