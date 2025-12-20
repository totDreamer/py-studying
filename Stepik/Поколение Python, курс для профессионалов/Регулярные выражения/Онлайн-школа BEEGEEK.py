from sys import stdin
from re import search

pattern = r'_\d+[A-Za-z]*_?\b'
for line in map(str.rstrip, stdin):
    if search(pattern, line):
        print(True)
    else:
        print(False)