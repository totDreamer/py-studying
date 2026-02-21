from itertools import chain
from random import shuffle


class RandomLooper:
    def __init__(self, *iterables):
        self.data = list(chain(*iterables))
        shuffle(self.data)
        self.iterable = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)


randomlooper = RandomLooper(["red", "blue", "green", "purple"])

print(list(randomlooper))
print(list(randomlooper))


colors = ["red", "blue", "green", "purple"]
shapes = ["square", "circle", "triangle", "octagon"]
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))
