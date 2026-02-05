class TextHandler:
    def __init__(self):
        self.words_list = []

    def add_words(self, text):
        self.words_list.extend(text.split())

    def get_shortest_words(self):
        self.min_length = len(min(self.words_list, default="", key=len))
        return list(filter(lambda x: len(x) == self.min_length, self.words_list))

    def get_longest_words(self):
        self.max_length = len(max(self.words_list, default="", key=len))
        return list(filter(lambda x: len(x) == self.max_length, self.words_list))


texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())


texthandler = TextHandler()

texthandler.add_words("do not be sorry")
texthandler.add_words("be")
texthandler.add_words("better")

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())


texthandler = TextHandler()

texthandler.add_words("The world will hold my trial for your sins")
texthandler.add_words("Never meant to see the sky never meant to live")

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
