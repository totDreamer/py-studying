class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *names):
        self.juniors.extend((name, "junior") for name in names)

    def add_senior(self, *names):
        self.seniors.extend((name, "senior") for name in names)

    def __iter__(self):
        yield from self.juniors
        yield from self.seniors


beegeek = DevelopmentTeam()

beegeek.add_junior("Timur")
beegeek.add_junior("Arthur", "Valery")
beegeek.add_senior("Gvido")
print(*beegeek, sep="\n")


beegeek = DevelopmentTeam()

print(len(list(beegeek)))


beegeek = DevelopmentTeam()

beegeek.add_junior("Timur")
beegeek.add_junior("Arthur", "Valery")
print(*beegeek, sep="\n")
