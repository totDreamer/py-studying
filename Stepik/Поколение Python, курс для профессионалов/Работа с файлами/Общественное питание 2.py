import json

in_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/food_services.json'
with open(in_path, 'r', encoding='UTF-8', newline='') as f:
    data = json.load(f)
    count_at_type = {}

    for building in data:
        type_o = building['TypeObject']
        name = building['Name']
        s_count = int(building['SeatsCount'])
        
        if type_o not in count_at_type:
            count_at_type[type_o] = [name, s_count]
        
        else:
            if count_at_type[type_o][1] < s_count:
                count_at_type[type_o] = [name, s_count]
    
    count_at_type = dict(sorted(count_at_type.items()))
    for k, v in count_at_type.items():
        print(f'{k}: {v[0]}, {v[1]}')