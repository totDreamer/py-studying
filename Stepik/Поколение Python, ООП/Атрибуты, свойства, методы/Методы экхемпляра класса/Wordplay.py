class Wordplay:
    def __init__(self, words=[]):
        self.words = words[:]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        char_set = set(c for c in args)
        return list(filter(lambda x: set(x).issubset(char_set), self.words))

    def avoid(self, *args):
        char_set = set(c for c in args)
        return list(filter(lambda x: char_set.isdisjoint(set(x)), self.words))


wordplay = Wordplay()

print(wordplay.words_with_length(1))
print(wordplay.only("a", "b", "c"))
print(wordplay.avoid("a", "b", "c"))


wordplay = Wordplay()

print(wordplay.words)
wordplay.add_word("bee")
wordplay.add_word("geek")
print(wordplay.words)


wordplay = Wordplay(["bee", "geek", "cool", "stepik"])

wordplay.add_word("python")
print(wordplay.words_with_length(4))


wordplay = Wordplay(["o", "to", "otto", "top", "t"])

print(wordplay.only("o", "t"))


wordplay = Wordplay(["a", "arthur", "timur", "bee", "geek", "python", "stepik"])

print(wordplay.words)
wordplay.add_word("stepik")
wordplay.add_word("bee")
wordplay.add_word("geek")
print(wordplay.words)
