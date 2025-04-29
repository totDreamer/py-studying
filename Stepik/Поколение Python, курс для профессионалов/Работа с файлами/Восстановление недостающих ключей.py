import json

in_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/people.json'
out_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/updated_people.json'
with open(in_path, 'r', encoding='UTF-8', newline='') as f, \
    open(out_path, 'w', encoding='UTF-8', newline='') as fo:
    data = json.load(f)
    all_keys = {}

    for i in data:
        for key in i.keys():
            all_keys[key] = all_keys.get(key, None)

    upd_data = [all_keys | i for i in data]
    json.dump(upd_data, fo)