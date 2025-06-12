from zipfile import ZipFile

def convert_bytes(size):
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

def convert_print(string):
    if string[-1] == '/':
        string = string[:-1]
    try:
        name = string.split('/')
        space = '  ' * (len(name) - 1)
        return f'{space}{name[-1]}'
    except:
        return string



z_path = '/home/user/py-studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/desktop.zip'
with ZipFile(z_path) as z_file:
    data = z_file.infolist()
    for f in data:
        if f.is_dir():
            print(convert_print(f.filename))
        else:
            print(f'{convert_print(f.filename)} {convert_bytes(f.file_size)}')