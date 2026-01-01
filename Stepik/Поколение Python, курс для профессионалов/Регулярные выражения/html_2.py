from sys import stdin
from re import search, finditer, findall, DOTALL

teg_pattern = r"<\w+.*?>"
data = stdin.read()
result = dict()

for line in finditer(teg_pattern, data, flags=DOTALL):
    key = search(r"<(\w+)[ >]?", line.group()).group(1)
    values = findall(r"\s([\w-]+)=", line.group())
    result[key] = sorted(values)

for key, values in sorted(result.items(), key=lambda x: x[0]):
    print(f"{key}: {', '.join(values)}")
