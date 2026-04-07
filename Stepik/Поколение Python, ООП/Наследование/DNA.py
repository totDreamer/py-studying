from collections import UserString


class DNA(UserString):
    chain_links = {"T": "A", "A": "T", "G": "C", "C": "G"}

    def __init__(self, chain):
        self.data = chain

    def __getitem__(self, index):
        char = self.data[index]
        return (char, self.__class__.chain_links[char])

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return super().__eq__(other)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return super().__add__(other.data)


dna = DNA("AGTC")

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])
print()


dna = DNA("AGT")

print(dna)
print(len(dna))
print("A" in dna)
print("C" in dna)
print()


dna1 = DNA("ACG")
dna2 = DNA("TTTAAT")
dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))
print()


dna1 = DNA("ACG")
dna2 = DNA("TTTAAT")
dna3 = DNA("TTTAAT")

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)
