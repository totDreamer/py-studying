n = int(input())
name_dict = {name.lower(): result for _ in range(n) for name, result in [input().split(': ')]}
m = int(input())
result_list = [input().lower() for _ in range(m)]
for result in result_list:
    if result not in name_dict:
        print('Не найдено')
    else:
        print(name_dict[result])