import json

in_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/countries.json'
out_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/religion.json'
with open(in_path, 'r', encoding='UTF-8', newline='') as f, \
    open(out_path, 'w', encoding='UTF-8', newline='') as fo:
    data = json.load(f)
    religion = {}

    for v in data:
        religion[v['religion']] = religion.get(v['religion'], [])
        religion[v['religion']].append(v['country'])

    json.dump(religion, fo, indent=6)