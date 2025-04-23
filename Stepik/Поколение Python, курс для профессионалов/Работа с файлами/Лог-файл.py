import arrow, csv

with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/name_log.csv', 'r', encoding='UTF-8', newline='') as f, \
     open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/new_name_log.csv', 'w', encoding='UTF-8', newline='') as f2:
    
    data = sorted(csv.DictReader(f), key=lambda x: (x['email'], arrow.get(x['dtime'], 'DD/MM/YYYY HH:mm')), reverse=True)
    new_data = []
    emails = []
    for row in data:
        if row['email'] not in emails:
            new_data.append(row)
            emails.append(row['email'])

    columns = new_data[0].keys()
    writer = csv.DictWriter(f2, fieldnames=columns)
    writer.writeheader()
    writer.writerows(new_data)