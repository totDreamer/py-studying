from sys import stdin
from re import search, IGNORECASE, MULTILINE

count = 0
for s in stdin:
    if search(r'beegeek', s, flags=IGNORECASE|MULTILINE):
        count += 1

print(count)