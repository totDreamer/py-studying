from collections import Counter

def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())

print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))