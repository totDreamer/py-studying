def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    suits = ["пик", "треф", "бубен", "червей"]
    suits.remove(suit)
    

    def make_deck():
        return (f'{v} {s}' for s in suits for v in card_values)

    def croupier():
        while True:
            yield from make_deck()

    return croupier()


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]
print(*cards)