import csv

def condense_csv(data, id_name):
    read_path = data
    write_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/condensed.csv'
    with open(read_path, 'r', encoding='UTF-8', newline='') as f, \
        open(write_path, 'w', encoding='UTF-8', newline='') as f2:

        r_data = csv.reader(f)
        merge_data = {}
        for row in r_data:
            name = row[0]
            merge_data[name] = merge_data.get(name, {})
            merge_data[name][row[1]] = row[2]
    
        converted_data = [{id_name: k, **merge_data[k]} for k in merge_data]
        columns = converted_data[0].keys()
        writer = csv.DictWriter(f2, fieldnames=columns)
        writer.writeheader()
        writer.writerows(converted_data)



condense_csv('/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/condense.csv', 'ID')

