from re import finditer

text, w = input(), input()
print(sum(1 for _ in finditer(rf'\b{w}\b', text)))