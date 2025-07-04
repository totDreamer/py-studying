from collections import Counter, defaultdict

def most_common(text):
    counter = Counter(text.lower().split())
    reversed_dict = defaultdict(list)
    for value, key in counter.items():
       reversed_dict[key].append(value)
    result = max((reversed_dict[max(reversed_dict)]))
    return result

print(most_common(input()))