from collections import Counter

def count_occurences(word, words):
    count = Counter(words.lower().split())
    return count[word.lower()]


word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))