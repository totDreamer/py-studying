from collections import Counter
import csv

path = '/home/totDreamer-/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/name_log.csv'
with open(path, 'r', encoding='UTF-8') as f:
    data = csv.DictReader(f)
    counter = Counter(line['email'] for line in data)
    for email, count in sorted(counter.items(), key=lambda x: x[0]):
        print(f'{email}: {count}')