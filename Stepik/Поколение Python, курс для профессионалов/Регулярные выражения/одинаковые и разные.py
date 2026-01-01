from re import finditer, IGNORECASE

word = input()[:-2]
text = input()

print(sum(1 for _ in finditer(fr'\b{word}[sz]e\b', text, flags=IGNORECASE)))