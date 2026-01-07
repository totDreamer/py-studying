from re import split


pattern = r"\s*[.,;]\s*"
print(*split(pattern, input()))
