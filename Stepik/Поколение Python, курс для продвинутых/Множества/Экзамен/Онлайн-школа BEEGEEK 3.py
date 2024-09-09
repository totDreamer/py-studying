m, n = int(input()), int(input())
mathematics = set(input() for _ in range(m))
informatics = set(input() for _ in range(n))
if len(mathematics.symmetric_difference(informatics)) != 0:
    print(len(mathematics.symmetric_difference(informatics)))
else:
    print('NO')