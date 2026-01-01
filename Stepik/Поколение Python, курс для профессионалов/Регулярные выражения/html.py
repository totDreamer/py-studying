from sys import stdin
from re import finditer, MULTILINE

pattern = r'<a\s+href="([^"]+)">(.+?)</a>'
data = stdin.read()

for line in finditer(pattern, data, flags=MULTILINE):
    print(*line.groups(), sep=", ")
