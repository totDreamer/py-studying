from re import finditer, IGNORECASE

word = input()
text = input()

print(sum(1 for _ in finditer(fr'\b{word[:-3]}ou?r\b', text, flags=IGNORECASE)))