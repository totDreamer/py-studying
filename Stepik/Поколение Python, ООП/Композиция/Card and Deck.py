from random import shuffle as r_shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    def __init__(self):
        self.cards = [
            Card(s, r)
            for s in "♣♢♡♠"
            for r in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        ]

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Перемешивать можно только полную колоду")
        r_shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError("Все карты разыграны")
        return self.cards.pop()

    def __str__(self):
        return f"Карт в колоде: {len(self.cards)}"


print(Card("♣", "4"))
print(Card("♡", "A"))
print(Card("♢", "10"))
print()


cards = Deck()

print(cards)
print(cards.deal())
print(cards.deal())
print(cards.deal())
print(type(cards.deal()))
print(cards)
print()


cards = Deck()

for _ in range(52):
    cards.deal()

try:
    cards.deal()
except ValueError as error:
    print(error)
print()


cards = Deck()

cards.deal()

try:
    cards.shuffle()
except ValueError as error:
    print(error)
