import json, arrow

path = 'D:/Python-Studying/Stepik/Поколение Python, курс для профессионалов/Работа с файлами/pools.json'
with open(path, 'r', encoding='UTF-8', newline='') as f:
    data = json.load(f)

    def filt_by_time(ob):
        start_time, end_time = ob["WorkingHoursSummer"]["Понедельник"].split('-')
        patt = 'HH:mm'
        if arrow.get(start_time, patt) <= arrow.get('10:00', patt) and arrow.get(end_time, patt) >= arrow.get('12:00', patt):
            return True
        else:
            return False
    
    def get_pool_size(ob):
        length, width = int(ob["DimensionsSummer"]["Length"]), int(ob["DimensionsSummer"]["Width"])
        return (length, width)

    sort_data = sorted([ob for ob in data if filt_by_time(ob)], key=get_pool_size, reverse=True)
    result = sort_data[0]
    
    print(f'{result["DimensionsSummer"]["Length"]}x{result["DimensionsSummer"]["Width"]}\n{result['Address']}')
    