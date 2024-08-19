value_1, value_2 = input(), input()
test_value = set(range(10))
if len(set(value_1 + value_2)) == len(test_value):
    print('YES')
else:
    print('NO')