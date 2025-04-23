import csv

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/salary_data.csv', 'r', encoding='UTF-8', newline='') as f:
    companies = csv.DictReader(f, delimiter=';')
    average = {}
    for c in companies:
        name = c['company_name']
        data = average.get(name, {'salary': 0, 'count': 0})
        data['salary'] += int(c['salary'])
        data['count'] += 1
        average[name] = data
    
    sorted_companies = sorted(average.items(), key=lambda x: x[1]['salary'] / x[1]['count'])

    for company in sorted_companies:
        print(company[0])