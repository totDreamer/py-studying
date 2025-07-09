def read_file(path):
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            data = f.read()
            print(data)
    except:
        print('Файл не найден')

read_file(input())