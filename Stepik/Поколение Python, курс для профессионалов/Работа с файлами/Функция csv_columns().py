import csv

def csv_columns(file):
    with open(file, 'r', encoding='UTF-8', newline='') as f:
        data = csv.DictReader(f, delimiter=';')
        data_dict = {}
        for row in data:
            for key, value in row.items():
                data_dict[key] = data_dict.get(key, [])
                data_dict[key].append(value)
        
        return data_dict
    

print(csv_columns('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/salary_data.csv'))