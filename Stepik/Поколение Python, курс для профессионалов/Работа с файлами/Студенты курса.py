import json, csv

in_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/students.json'
out_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/students.csv'
with open(in_path, 'r', encoding='UTF-8', newline='') as f, \
    open(out_path, 'w', encoding='UTF-8', newline='') as fo:
    data = json.load(f)
    sort_data = []

    for ob in data:
        age = int(ob['age'])
        progress = int(ob['progress'])
        if age >= 18 and progress >= 75:
            sort_data.append({'name': ob['name'], 'phone': ob['phone']})
    
    sort_data = sorted(sort_data, key=lambda x: x['name'])
    columns = sort_data[0].keys()
    writer = csv.DictWriter(fo, fieldnames=columns)
    writer.writeheader()
    writer.writerows(sort_data)