from itertools import permutations

def rev(line):
    return set(''.join(l) for l in permutations(list(line)))

data = rev(input())

for obj in sorted(data):
    print(obj)

