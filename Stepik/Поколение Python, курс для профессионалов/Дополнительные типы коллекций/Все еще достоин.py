from sys import stdin
from collections import defaultdict

data = stdin.readlines()
results = defaultdict(int)
for line in data:
    key, value = line.split()
    results[key] = int(value)
print(sorted(results, key=lambda x: results[x])[1])