class DictItemsIterator:
    def __init__(self, data):
        self.data = iter(data.items())

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.data)

pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)

data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
pairs = DictItemsIterator(data)
print(*pairs)