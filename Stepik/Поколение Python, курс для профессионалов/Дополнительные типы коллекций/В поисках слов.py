from collections import Counter

def most_common(text):
    text = text.lower().split()
    return Counter(text).most_common(1)[0][0]

print(most_common(input()))