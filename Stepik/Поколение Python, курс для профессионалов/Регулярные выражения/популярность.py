from sys import stdin
from re import fullmatch, search

def scoring(line):
    if fullmatch(r'\bbeegeek.*beegeek\b', line):
        return 3
    if fullmatch(r'\bbeegeek.+|.+beegeek\b', line):
        return 2
    if search(r'beegeek', line):
        return 1
    return 0

result = 0
for line in map(str.rstrip, stdin):
    result += scoring(line)

print(result)