import csv, json

in_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/playgrounds.csv'
out_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/addresses.json'
with open(in_path, 'r', encoding='UTF-8', newline='') as f, \
    open(out_path, 'w', encoding='UTF-8', newline='') as fo:
    data = csv.DictReader(f, delimiter=';')
    addresses = {}

    for r in data:
        addresses[r['AdmArea']] = addresses.get(r['AdmArea'], {})
        addresses[r['AdmArea']][r['District']] = addresses[r['AdmArea']].get(r['District'], []) + [r['Address']]
    
    json.dump(addresses, fo, indent=6, ensure_ascii=False)