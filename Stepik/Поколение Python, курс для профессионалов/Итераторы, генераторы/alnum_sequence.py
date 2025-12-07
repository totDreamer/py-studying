from itertools import cycle

def alnum_sequence():
    yield from cycle(elem for ob in zip(range(1, 28), map(chr, range(65, 91))) for elem in ob)

alnum = alnum_sequence()
print(*(next(alnum) for _ in range(55)))