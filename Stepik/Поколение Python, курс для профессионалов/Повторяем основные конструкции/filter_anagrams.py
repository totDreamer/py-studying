def filter_anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))