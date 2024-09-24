first_string, second_string = input(), input()
first_dict = {}
second_dict = {}
for i in first_string:
    first_dict.setdefault(i, 0)
    first_dict[i] += 1
for j in second_string:
    second_dict.setdefault(j, 0)
    second_dict[j] += 1
if first_dict == second_dict:
    print('YES')
else:
    print('NO')