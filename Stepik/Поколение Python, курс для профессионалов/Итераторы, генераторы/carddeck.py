class CardDeck:
    def __init__(self):
        suits = ("пик", "треф", "бубен", "червей")
        values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.full_deck = iter(f'{v} {s}' for s in suits for v in values)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.full_deck)


cards = CardDeck()
print(next(cards))
print(next(cards))


cards = list(CardDeck())
print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])