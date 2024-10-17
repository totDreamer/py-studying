name_numbers = {}
for _ in range(int(input())):
    *numbers, name = input().split()
    name_numbers.setdefault(name.lower(), []).extend(numbers)
for _ in range(int(input())):
    name = input().lower()
    if name not in name_numbers:
        print('абонент не найден')
    else:
        print(*name_numbers[name])