first_string, second_string = input().lower(), input().lower()
first_dict = {}
second_dict = {}
for i in first_string:
    if i.isalpha():
        first_dict.setdefault(i, 0)
        first_dict[i] += 1
for j in second_string:
    if j.isalpha():
        second_dict.setdefault(j, 0)
        second_dict[j] += 1
if first_dict == second_dict:
    print('YES')
else:
    print('NO')