import json

def des_file(path):
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return "Файл не найден"
    except:
        return "Ошибка при десериализации"

print(des_file(input()))