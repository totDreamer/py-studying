print(*sorted([input() for _ in range(int(input()))],
              key=lambda s: (sum(ord(c.upper()) - ord('A') for c in s), s)), sep='\n')


