first_num, second_num = set(input()), set(input())
if first_num.issuperset(second_num) == True:
    print('YES')
else:
    print('NO')