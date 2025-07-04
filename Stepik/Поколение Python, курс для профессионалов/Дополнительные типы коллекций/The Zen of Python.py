from collections import Counter

path = '/home/user/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/pythonzen.txt'
with open(path, 'r', encoding='UTF-8') as f:
    data = Counter(filter(lambda x: x.isalpha(), f.read().lower()))
    for char, count in sorted(data.items()):
        print(f'{char}: {count}')