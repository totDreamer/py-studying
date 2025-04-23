import csv

with open('/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/titanic.csv', 'r', encoding='UTF-8', newline='') as f:
    data = csv.DictReader(f, delimiter=';')
    small_survivors = sorted([h for h in data if h['survived']=='1' and float(h['age'])<18.0], key=lambda x: x['sex'] == 'male', reverse=True)
    for name in small_survivors:
        print(name['name'])