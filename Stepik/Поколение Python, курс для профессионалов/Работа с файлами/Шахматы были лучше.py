from zipfile import ZipFile
import json

z_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/data.zip'
with ZipFile(z_path) as z_file:
    names = []
    
    for file_name in z_file.namelist():
        if file_name.endswith('.json'):
            with z_file.open(file_name, 'r') as j_file:
                try:
                    d = json.loads(j_file.read())
                    if d['team'] == 'Arsenal':
                        names.append((d['first_name'], d['last_name']))
                except:
                    continue

    for n in sorted(names, key=lambda x: (x[0], x[1])):
        print(*n)