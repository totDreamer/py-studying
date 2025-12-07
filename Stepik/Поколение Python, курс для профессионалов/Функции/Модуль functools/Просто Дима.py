from sys import stdin
from functools import lru_cache

@lru_cache
def sorted_words(word):
    return ''.join(sorted(list(word)))

for word in stdin:
    print(sorted_words(word.strip()))