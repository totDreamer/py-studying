word_count = {}
for word in input().split():
    word_count[word] = word_count.get(word, 0) + 1
    print(word_count[word], end= ' ')
