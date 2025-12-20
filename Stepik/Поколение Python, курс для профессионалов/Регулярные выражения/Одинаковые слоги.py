from re import search
from sys import stdin

pattern = r'\b(.+)\1\b'
for line in map(str.rstrip, stdin):
    if search(pattern, line):
        print(line)

