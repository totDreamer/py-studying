from re import findall, search
from sys import stdin

b, g = 0, 0
for line in map(str.rstrip, stdin):
    if search(r'\bgeek\b', line):
        g += 1
    if len(findall(r'bee', line)) >= 2:
        b += 1

print(b, g, sep='\n')