class Alphabet:
    def __init__(self, language):
        self.language = language

        if self.language == 'ru':
            self.alphabet = iter(chr(num) for num in range(1072, 1104))
        else:
            self.alphabet = iter(chr(num) for num in range(97, 123))
        
        self.reserve = tuple(self.alphabet)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.alphabet)
        except StopIteration:
            self.alphabet = iter(self.reserve)
            return next(self.alphabet)



ru_alpha = Alphabet('ru')
print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))


en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(28)]
print(*letters)