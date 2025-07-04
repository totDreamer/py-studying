from collections import Counter

lens = Counter(len(word) for word in input().split())
for key, value in sorted(lens.items(), key=lambda x: x[1]):
    print(f'Слов длины {key}: {value}')