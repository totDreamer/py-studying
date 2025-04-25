import csv

input_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/prices.csv'

with open(input_path, 'r', encoding='UTF-8', newline='') as f:
    data = csv.DictReader(f, delimiter=';')
    chipest_in_market = {}
    for row in data:
        name = row['Магазин']
        chipest_in_market[name] = chipest_in_market.get(name, ())
        value = min(row.items(), key=lambda x: (int(x[1]) if x[1].isdigit() else 10000, x[0]))
        chipest_in_market[name] = value

    sorted_chip = sorted(chipest_in_market.items(), key=lambda x: (int(x[1][1]), x[1][0], x[0]))
    chipest_market, chipest_item = sorted_chip[0][0], sorted_chip[0][1][0]

    
    print(f'{chipest_item}: {chipest_market}')