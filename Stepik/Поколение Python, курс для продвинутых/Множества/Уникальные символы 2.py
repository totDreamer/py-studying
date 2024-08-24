n = int(input())
unique_s = set()
for _ in range(n):
    word = set(input().lower())
    unique_s.update(word)
print(len(unique_s))