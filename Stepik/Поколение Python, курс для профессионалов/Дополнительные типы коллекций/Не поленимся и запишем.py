from collections import Counter

count = Counter(input().split(','))

for word, count in sorted(count.items()):
    print(f'{word}: {count}')