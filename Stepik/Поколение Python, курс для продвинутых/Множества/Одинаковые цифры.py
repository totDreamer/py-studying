first_num, second_num = set(input()), set(input())
if first_num.isdisjoint(second_num) == True:
    print('NO')
else:
    print('YES')