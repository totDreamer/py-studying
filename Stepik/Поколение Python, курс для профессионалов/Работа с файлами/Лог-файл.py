import arrow, csv

input_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/name_log.csv'
output_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/new_name_log.csv'

latest_by_email = {}

with open(input_path, 'r', encoding='UTF-8', newline='') as f, \
     open(output_path, 'w', encoding='UTF-8', newline='') as f2:
    
    reader = csv.DictReader(f)

    for row in reader:
        email = row['email']
        dt = arrow.get(row['dtime'], 'DD/MM/YYYY HH:mm')

        if email not in latest_by_email or dt > arrow.get(latest_by_email[email]['dtime'], 'DD/MM/YYYY HH:mm'):
            latest_by_email[email] = row

    sorted_rows = sorted(latest_by_email.values(), key=lambda x: (x['email'], arrow.get(x['dtime'], 'DD/MM/YYYY HH:mm')))

    writer = csv.DictWriter(f2, fieldnames=sorted_rows[0].keys())
    writer.writeheader()
    writer.writerows(sorted_rows)