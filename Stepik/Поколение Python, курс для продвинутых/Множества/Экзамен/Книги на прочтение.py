m, n = int(input()), int(input())
home_book = set([input() for _ in range(m)])
library_list = [input() for _ in range(n)]
for book in library_list:
    if book in home_book:
        print('YES')
    else:
        print('NO')