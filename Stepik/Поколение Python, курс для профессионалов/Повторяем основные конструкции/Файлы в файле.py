with open('D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Повторяем основные конструкции/files.txt', encoding='UTF-8') as f:
    files_extension = {}
    files_extension_size = {}

    def convert_to_kb(value, value_type):
        value = int(value)
        result = 0
        if value_type == 'B':
            result = value
        elif value_type == 'KB':
            result = value * 1024
        elif value_type == 'MB':
            result = value * 1024**2
        elif value_type == 'GB':
            result = value * 1024**3
        return result
    
    def compose_result(ext):
        size = files_extension_size[ext]
        if size < 1024:
            size = f'{size} B'
        elif size < 1024**2:
            size = f'{round(size / 1024)} KB'
        elif size < 1024**3:
            size = f'{round(size / 1024**2)} MB'
        else:
            size = f'{round(size / 1024**3)} GB'
        for name in files_extension[ext]:
            print(name)
        print('----------')
        print(f'Summary: {size}')
        print()

    for line in f:
        line = line.split()
        ext = line[0][line[0].rfind('.') + 1:]

        files_extension[ext] = files_extension.get(ext, [])
        files_extension[ext].append(line[0])

        files_extension_size[ext] = files_extension_size.get(ext, 0)
        files_extension_size[ext] += convert_to_kb(line[-2], line[-1])

    
    for key, value in sorted(files_extension.items()):
        files_extension[key] = sorted(value)
        compose_result(key)