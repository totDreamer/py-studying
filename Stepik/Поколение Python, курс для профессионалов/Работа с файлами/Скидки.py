import csv

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/sales.csv', 'r', encoding='UTF-8', newline='') as f:
    rows = csv.DictReader(f, delimiter=';')
    real_disc = [row for row in rows if int(row['old_price']) > int(row['new_price'])]
    for item in real_disc:
        print(item['name'])