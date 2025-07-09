from collections import defaultdict

def flip_dict(dict_of_lists):
    flip = defaultdict(list)
    for key, values in dict_of_lists.items():
        for value in values:
            flip[value].append(key)
    return flip

print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))