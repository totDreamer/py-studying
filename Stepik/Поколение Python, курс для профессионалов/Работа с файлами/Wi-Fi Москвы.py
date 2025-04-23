import csv

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/wifi.csv', 'r', encoding='UTF-8', newline='') as f:
    data = csv.DictReader(f, delimiter=';')
    dist_count = {}

    for row in data:
        name = row['district']
        dist_count[name] = dist_count.get(name, 0) + int(row['number_of_access_points'])

    for d in sorted(dist_count.items(), key=lambda x: (-x[1], x[0])):
        print(*d, sep=': ')