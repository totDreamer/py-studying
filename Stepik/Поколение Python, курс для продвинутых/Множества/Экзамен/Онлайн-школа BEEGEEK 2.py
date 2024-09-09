m, n = int(input()), int(input())
mathematics = set(input() for _ in range(m))
informatics = set(input() for _ in range(n))
print(len(mathematics - informatics))