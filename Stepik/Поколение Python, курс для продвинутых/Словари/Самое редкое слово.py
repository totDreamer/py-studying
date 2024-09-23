string = [''.join(sym for sym in word if sym.isalpha()) for word in input().lower().split()]
word_count = {}
for word in string:
    word_count.setdefault(word, 0)
    word_count[word] += 1
result = {}
for word, count in word_count.items():
    result.setdefault(count, []).append(word)
min_count = min(result[min(result)])
print(min_count)