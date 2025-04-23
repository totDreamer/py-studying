import csv

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/data.csv', 'r', encoding='UTF-8', newline='') as f:
    data = list(csv.reader(f))
    del data[0]
    dom_count = {}
    for row in data:
        domain = row[2][row[2].index('@')+1:]
        dom_count[domain] = dom_count.get(domain, 0) 
        dom_count[domain] += 1
    sort_dom_count = [f'{line[0]},{line[1]}\n' for line in sorted(dom_count.items(), key=lambda x: (x[1], x[0]))]
    
    with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/domain_usage.csv', 'w', encoding='UTF-8', newline='') as f2:
        f2.write('domain,count\n')
        f2.writelines(sort_dom_count)