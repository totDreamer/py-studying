from collections import Counter, defaultdict

def most_common(text):
    counter = Counter(text.lower().split())
    reversed_dict = defaultdict(list)
    for value, key in counter.items():
       reversed_dict[key].append(value)
    result = ', '.join(sorted(reversed_dict[min(reversed_dict)]))
    return result

print(most_common(input()))