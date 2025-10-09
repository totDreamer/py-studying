def zip_longest(*lists, fill=None):
    max_len = len(max(lists, key = len))
    new_lists = []
    for l in lists:
        while len(l) != max_len:
            l.append(fill)
        new_lists.append(l)
    return list(zip(*new_lists))


data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))