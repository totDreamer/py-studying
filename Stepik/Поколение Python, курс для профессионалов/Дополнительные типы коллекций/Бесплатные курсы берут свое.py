import csv, json
from collections import Counter

def count_for_quarter(qfile):
    f = [line.strip().split(',') for line in qfile.readlines()]
    q_count = Counter()
    for line in f[1:]:
        q_count.update(Counter({line[0]: sum(int(c) for c in line[1:])}))
    return q_count

def sum_for_quarters(total_count, f_price):
    price = json.load(f_price)
    result = 0
    for name, count in total_count.items():
        result += price[name] * count

    return result

path_1 = '/home/totDreamer-/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/quarter1.csv'
path_2 = '/home/totDreamer-/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/quarter2.csv'
path_3 = '/home/totDreamer-/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/quarter3.csv'
path_4 = '/home/totDreamer-/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/quarter4.csv'
pr_path = '/home/totDreamer-/study/py-studying/Stepik/Поколение Python, курс для профессионалов/Дополнительные типы коллекций/prices.json'
with open(path_1, 'r', encoding='UTF-8') as q1, \
     open(path_2, 'r', encoding='UTF-8') as q2, \
     open(path_3, 'r', encoding='UTF-8') as q3, \
     open(path_4, 'r', encoding='UTF-8') as q4, \
     open(pr_path, 'r', encoding='UTF-8') as pr:
        q_list = [q1, q2, q3, q4]
        total_count = Counter()
        for q in q_list:
            total_count.update(count_for_quarter(q))

        print(sum_for_quarters(total_count, pr))