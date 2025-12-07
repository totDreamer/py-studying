from itertools import groupby

def grouper(words: str):
    data = groupby(sorted(words.split(), key=lambda x: (len(x), x)), key=len)
    yield from data

for group, data in grouper(input()):
    print(f'{group} -> {', '.join(data)}')