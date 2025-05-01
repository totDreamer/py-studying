import json

in_path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/food_services.json'
with open(in_path, 'r', encoding='UTF-8', newline='') as f:
    data = json.load(f)
    count_at_district = {}
    count_at_web = {}

    for building in data:
        district = building['District']
        isnet = building['IsNetObject']
        web = building['OperatingCompany']
        count_at_district[district] = count_at_district.get(district, 0) + 1
        if isnet == 'да':
            count_at_web[web] = count_at_web.get(web, 0) + 1 

    d, d_count = max(count_at_district.items(), key=lambda x: x[1])
    w, w_count = max(count_at_web.items(), key=lambda x: x[1])
    print(f'{d}: {d_count}\n{w}: {w_count}')